import unittest

from .messages import containsThanks

class TestUtilsMessages(unittest.TestCase):
    def test_contains_thanks_happy_path(self):
        text = "i would like to thank you"
        self.assertTrue(containsThanks(text))

    def test_contains_thanks_happy_path_2(self):
        text = "thanks!"
        self.assertTrue(containsThanks(text))

    def test_contains_thanks_happy_path(self):
        text = "i do not contain any gratitude"
        self.assertFalse(containsThanks(text))

if __name__ == '__main__':
    unittest.main()
