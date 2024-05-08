import unittest
from text_change import upper_convertion


class TestChangeText(unittest.TestCase):
    def test_upper_text(self):
        word = "hello"
        result = upper_convertion(word)
        self.assertEqual(result, 'HELLO')

if __name__ == '__main__':
    unittest.main()