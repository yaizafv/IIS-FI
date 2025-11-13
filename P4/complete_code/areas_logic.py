# 13:26
def calculate_square_area(side_length):
    """Returns the area of a square based on it's side

    Args:
        side_length(float): The length of the side.

    Returns:
        float: The area of the square.

    Examples:
        >>> calculate_square_area(3)
        9
        >>> calculate_square_area(2)
        4
        >>> calculate_square_area(0)
        0
        >>> calculate_square_area(-2)
        Traceback (most recent call last):
        ...
        ValueError: The side length must not be negative.
    """
    if side_length < 0:
        raise ValueError("The side length must not be negative.")
    area = calculate_rectangle_area(side_length, side_length)
    return area


# 13:39


def calculate_rectangle_area(height, width):
    """Returns the area of a rectangle given it's height and width.

    Args:
        height(float): The height of the rectangle.
        width(float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.

    Examples:
        >>> calculate_rectangle_area(3, 4)
        12
        >>> calculate_rectangle_area(3, 0)
        0
        >>> calculate_rectangle_area(-3, 2)
        Traceback (most recent call last):
        ...
        ValueError: The height and width must be positive.
    """
    if height < 0 or width < 0:
        raise ValueError("The height and width must be positive.")
    area = height * width
    return area

def calculate_triangle_area(base, height):
    """Returns the area of a triangle given it's base and height.

    Args:
        base(float): The base of the triangle.
        height(float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    Examples:
        >>> calculate_triangle_area(3, 4)
        6.0
        >>> calculate_triangle_area(3, 0)
        0.0
        >>> calculate_triangle_area(-3, 2)
        Traceback (most recent call last):
        ...
        ValueError: The base and height must be positive.
    """
    if base < 0 or height < 0:
        raise ValueError("The base and height must be positive.")
    area = calculate_rectangle_area(base, height) / 2
    return area

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
