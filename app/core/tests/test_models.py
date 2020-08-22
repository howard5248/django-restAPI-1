from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@gmail.com', password='testpassword'):
    '''Create a sample user'''
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test to create a new user with an email is sucessful'''
        email = 'howard@gmail.com'
        password = 'Abcd=1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''test the email for a new user is normalized'''
        email = 'howard@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'aaaaaaa')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''test creating user with no email raise error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'aaaaaaa')

    def test_create_new_superuser(self):
        '''test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'aaaaaaa'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        '''Test the tag string representation'''
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
