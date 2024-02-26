import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        # Create a square instance for testing
        self.square = Square(10, 5, 5, 1)

    def test_init(self):
        # Test initialization of Square instance
        self.assertEqual(self.square.size, 10)
        
        self.assertEqual(self.square.x, 5)
        self.assertEqual(self.square.y, 5)
        self.assertEqual(self.square.id, 1)

    def test_str(self):
        # Test string representation of Square instance
        self.assertEqual(str(self.square), "[Square] (1) 5/5 - 10")

    def test_update(self):
        # Test update method
        self.square.update(20, 10, 15, 2)
        self.assertEqual(str(self.square), "[Square] (2) 15/2 - 10")

    def test_to_dictionary(self):
        # Test conversion to dictionary
        self.assertEqual(self.square.to_dictionary(), {'id': 1, 'size': 10, 'x': 5, 'y': 5})

if __name__ == '__main__':
    unittest.main()
