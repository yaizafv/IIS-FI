def calculate_summatory_while(initial_number, final_number):
    """Receives two numbers and returns the sum of all numbers from initial_number to final_number.
    Both numbers are included in the sum.

    Args:
        initial_number (int): The starting number of the range.
        final_number (int): The ending number of the range.
    Returns:
        int: The sum of all numbers from initial_number to final_number.
    Exception:
        ValueError: If initial_number is greater than final_number.
    Examples:
        >>> calculate_summatory_while(1, 5)
        15
        >>> calculate_summatory_while(1, 10)
        55
        >>> calculate_summatory_while(5, 5)
        5
        >>> calculate_summatory_while(10, 1)
        Traceback (most recent call last):
        ...
        ValueError: initial_number (10) is greater than final_number (1).
    """

    if initial_number > final_number:
        raise ValueError(f"initial_number ({initial_number}) is greater than final_number ({final_number}).")
    result = 0

    while initial_number <= final_number:
        result += initial_number
        initial_number += 1

    return result


def calculate_summatory(initial_number, final_number):
    """Receives two numbers and returns the sum of all numbers from initial_number to final_number.
    Both numbers are included in the sum.

    Args:
        initial_number (int): The starting number of the range.
        final_number (int): The ending number of the range.
    Returns:
        int: The sum of all numbers from initial_number to final_number.
    Exception:
        ValueError: If initial_number is greater than final_number.
    Examples:
        >>> calculate_summatory(1, 5)
        15
        >>> calculate_summatory(1, 10)
        55
        >>> calculate_summatory(5, 5)
        5
        >>> calculate_summatory(10, 1)
        Traceback (most recent call last):
        ...
        ValueError: initial_number (10) is greater than final_number (1).
    """
    if initial_number > final_number:
        raise ValueError(f"initial_number ({initial_number}) is greater than final_number ({final_number}).")
    result = 0

    for i in range(initial_number, final_number + 1):
        result += i

    return result


def concatenate_numbers_ascending(initial_number, final_number):
    """Receives two numbers and returns a string with the numbers from initial_number to final_number.

    Args:
        initial_number (int): The starting number of the range.
        final_number (int): The ending number of the range.
    Returns:
        str: A string with the numbers from initial_number to final_number, both included.
    Exception:
        ValueError: If initial_number is greater than final_number.
    Examples:
        >>> concatenate_numbers_ascending(2, 5)
        '2345'
        >>> concatenate_numbers_ascending(5, 5)
        '5'
        >>> concatenate_numbers_ascending(5, 2)
        Traceback (most recent call last):
        ...
        ValueError: initial_number (5) is greater than final_number (2).
    """
    if initial_number > final_number:
        raise ValueError(f"initial_number ({initial_number}) is greater than final_number ({final_number}).")
    result = ""

    for current_number in range(initial_number, final_number + 1):
        result += str(current_number)

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
