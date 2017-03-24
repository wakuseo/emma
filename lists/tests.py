from django.test import TestCase

class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(10 + 23, 458)
# Create your tests here.
