import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        # Create a rectangle instance for testing
        self.rect = Rectangle(10, 20, 5, 5, 1)

    def test_init(self):
        # Test initialization of Rectangle instance
        self.assertEqual(self.rect.width, 10)
        self.assertEqual(self.rect.height, 20)
        self.assertEqual(self.rect.x, 5)
        self.assertEqual(self.rect.y, 5)
        self.assertEqual(self.rect.id, 1)

    def test_str(self):
        # Test string representation of Rectangle instance
        self.assertEqual(str(self.rect), "[Rectangle] (1) 5/5 - 10/20")

    def test_area(self):
        # Test calculation of area
        self.assertEqual(self.rect.area(), 200)

    def test_display(self):
        # Test display method
        expected_output = "\n\n\n\n\n     ##########\n     ##########\n     ##########\n     ##########\n     ##########\n"
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update(self):
        # Test update method
        self.rect.update(20, 30, 10, 15, 2)
        self.assertEqual(str(self.rect), "[Rectangle] (2) 15/2 - 20/30")

    def test_to_dictionary(self):
        # Test conversion to dictionary
        self.assertEqual(self.rect.to_dictionary(), {'id': 1, 'width': 10, 'height': 20, 'x': 5, 'y': 5})

if __name__ == '__main__':
    unittest.main()
