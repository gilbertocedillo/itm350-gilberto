# Sample function
def multiply(a, b):
    return a * b

# Unit test using Given-When-Then pattern
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_multiply(self):
        # Given
        a = 3
        b = 7
        expected = 21

        # When
        result = multiply(a, b)

        # Then
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
