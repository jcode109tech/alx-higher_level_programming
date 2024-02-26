#!\usr\bin\python3


from models.base import Base, Rectangle, Square

# Test save_to_file_csv and load_from_file_csv methods
def test_csv_methods():
    # Create some rectangles and squares
    rectangles = [Rectangle(10, 20), Rectangle(5, 15, 3, 8)]
    squares = [Square(5), Square(8, 2, 4)]

    # Save objects to CSV
    Base.save_to_file_csv(rectangles)
    Base.save_to_file_csv(squares)

    # Load objects from CSV
    loaded_rectangles = Base.load_from_file_csv(Rectangle)
    loaded_squares = Base.load_from_file_csv(Square)

    # Compare loaded objects with original objects
    assert len(loaded_rectangles) == len(rectangles)
    assert len(loaded_squares) == len(squares)

    for i in range(len(rectangles)):
        assert loaded_rectangles[i].to_dictionary() == rectangles[i].to_dictionary()

    for i in range(len(squares)):
        assert loaded_squares[i].to_dictionary() == squares[i].to_dictionary()

    print("CSV methods test passed successfully.")

# Test draw method
def test_draw_method():
    # Create some rectangles and squares
    rectangles = [Rectangle(100, 50, 0, 0), Rectangle(80, 30, -50, 100)]
    squares = [Square(70, 100, -50), Square(50, -100, -50)]

    # Draw rectangles and squares
    Base.draw(rectangles, squares)

    print("Draw method test passed successfully.")

if __name__ == "__main__":
    test_csv_methods()
    test_draw_method()
