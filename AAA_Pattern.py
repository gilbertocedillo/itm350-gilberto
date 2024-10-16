# Let's assume we have a simple function in our backend code
def add(a, b):
    return a + b

# Our unit test using the AAA pattern
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        # Arrange
        a = 5
        b = 10
        expected = 15

        # Act
        result = add(a, b)

        # Assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
