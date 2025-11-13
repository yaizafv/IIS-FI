import user_io
import vectors_logic


def ask_vector(message):
    """Request the user the coordinates for a vector as integers.

    Args:
        message(str): The message for the user.

    Returns:
        tuple(int, int): A vector with coordinates x and y

    Raises:
        ValueError: If any of the coordinates is not an int.
    """
    print(message)
    vector_x = user_io.ask_integer("Introduce x coordinate: ")
    vector_y = user_io.ask_integer("Introduce y coordinate: ")

    vector = (vector_x, vector_y)

    return vector


def main():
    """Main function"""

    vector1 = ask_vector("Introduce vector 1")
    vector2 = ask_vector("Introduce vector 2")

    added_vector = vectors_logic.add_vectors(vector1, vector2)
    print(f'The added vector is {added_vector}')
    
    substracted_vector = vectors_logic.substract_vectors(vector1, vector2)
    print(f'The substracted vector is {substracted_vector}')
    
    scalar = user_io.ask_integer("Introduce a scalar to multiply both vectors: ")
    multiplied_vector1 = vectors_logic.multiply_vector_by_scalar(vector1, scalar)
    multiplied_vector2 = vectors_logic.multiply_vector_by_scalar(vector2, scalar)
    
    print(f'The vector1 multiplied by {scalar} is {multiplied_vector1}')
    print(f'The vector2 multiplied by {scalar} is {multiplied_vector2}')


if __name__ == "__main__":
    main()
