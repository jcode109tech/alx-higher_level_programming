#!/urs/bin/python3

"""
    A function that prints a square with the character #.
"""

def print_square(size):
    """
    Prints a square with the character '#' of given size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if size is a float less than 0.
        ValueError: If size is less than 0.

    Returns:
        None
    """
    # Check if size is an integer
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


