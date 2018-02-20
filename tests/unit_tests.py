import unittest
from OneMoreLight.OneMoreLight.user_input import clean_user_input

class UnitTests(unittest.TestCase):
    def test_build(self):
        self.assertEqual(True, True, "True=True")

    def test_clean_user_input(self):
        dirty_string = "clean1_!@#$"
        clean_string = "clean1"
        self.assertEqual(clean_user_input(dirty_string), clean_string, "Sanitation complete")




