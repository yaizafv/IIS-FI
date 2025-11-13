def ask_integer(message):
    """Requests an integer to the user.

    Args:
        message(str): The prompt for the user.

    Returns:
        int: The integer introduced by the user.

    Raises:
        ValueError: If the user does not type an integer.
    """
    integer_text = input(message)
    integer = int(integer_text)
    return integer

def ask_positive_integer(message):
    """Requests an integer to the user.

    Args:
        message(str): The prompt for the user.

    Returns:
        int: The integer introduced by the user.

    Raises:
        ValueError: If the user does not type an integer, or is not positive.
    """
    integer = ask_integer(message)

    if integer < 0:
        raise ValueError("The introduced integer must be positive.")
    
    return integer
