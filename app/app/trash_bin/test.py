from django.test import TestCase

from app.calc import add


class CalcTest(TestCase):

    def test_add_number(self):
        """Simple try test"""
        self.assertEqual(add(3, 8), 11)
