def add_vectors(vector1, vector2):
    """Returns a new vector resulting in the sum of two vectors.

    Args:
        vector1 (tuple(float, float)): A tuple with coordinates x and y of vector 1.
        vector2 (tuple(float, float)): A tuple with coordinates x and y of vector 2.

    Returns:
        tuple(float, float): A new vector resulting in the sum of two vectors.

    Examples:
        >>> add_vectors((2, 3), (3, 10))
        (5, 13)
    """
    vector1_x, vector1_y = vector1
    vector2_x, vector2_y = vector2

    new_vector_x = vector1_x + vector2_x
    new_vector_y = vector1_y + vector2_y

    new_vector = (new_vector_x, new_vector_y)

    return new_vector

def substract_vectors(vector1, vector2):
    """Returns a new vector resulting in the subtraction of vector2 from vector1.
    
    Args:
        vector1 (tuple(float, float)): A tuple with coordinates x and y of vector 1.
        vector2 (tuple(float, float)): A tuple with coordinates x and y of vector 2.
    Returns:
        tuple(float, float): A new vector resulting in the subtraction of vector2 from vector1.
    Examples:
        >>> substract_vectors((5, 10), (2, 3))
        (3, 7)
        >>> substract_vectors((2, 3), (5, 10))
        (-3, -7)
        >>> substract_vectors((0, 0), (0, 0))
        (0, 0)
    """
    vector1_x, vector1_y = vector1
    vector2_x, vector2_y = vector2

    new_vector_x = vector1_x - vector2_x
    new_vector_y = vector1_y - vector2_y

    new_vector = (new_vector_x, new_vector_y)

    return new_vector

def multiply_vector_by_scalar(vector, scalar):
    """Returns a new vector resulting in the multiplication of a vector by a scalar.

    Args:
        vector (tuple(float, float)): A tuple with coordinates x and y of the vector.
        scalar (float): The scalar to multiply the vector by.

    Returns:
        tuple(float, float): A new vector resulting from the multiplication of the original vector by the scalar.

    Examples:
        >>> multiply_vector_by_scalar((2, 3), 2)
        (4, 6)
        >>> multiply_vector_by_scalar((2, 3), 0)
        (0, 0)
        >>> multiply_vector_by_scalar((2, 3), -1)
        (-2, -3)
    """
    vector_x, vector_y = vector

    new_vector_x = vector_x * scalar
    new_vector_y = vector_y * scalar

    new_vector = (new_vector_x, new_vector_y)

    return new_vector



if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
