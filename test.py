import unittest
from main import to_upper

class MytestCase(unittest.TestCase):
    def test_to_upper(self):
        name = 'gupta'
        upper_name = to_upper(name)
        self.assertEqual(upper_name, 'GUPTA')

if __name__ == "__main__":
    unittest.main()
