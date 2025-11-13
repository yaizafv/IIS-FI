import math

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


def count_numbers_ascending(initial_number, final_number):
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


def calculate_mcd(dividend, divisor):
    """Computes the maximum common divisor using the Euclidean algorithm.

    Args:
        number_a (int): the first integer.
        number_b (int): the second integer.
    Returns:
        int: the mcd.
    Examples:
        >>> calculate_mcd(4, 6)
        2
        >>> calculate_mcd(15, 45)
        15
        >>> calculate_mcd(12, 8)
        4
        >>> calculate_mcd(150, 340)
        10
    """
    # So that it works with negative numbers
    dividend = abs(dividend)
    divisor = abs(divisor)

    result = dividend

    while divisor != 0:
        remainder = result % divisor
        result = divisor
        divisor = remainder

    return result


def calculate_factorial(n):
    """calculate_factorial: returns the factorial of a positive integer.
    
    Args:
        n (int): the positive integer.
    Returns:
        int: the value of the factorial of n.
    Exception:
        ValueError when n is either negative or not an int.
    Examples:
        >>> calculate_factorial(0.5)
        Traceback (most recent call last):
        ...
        ValueError: calculate_factorial(0.5), 0.5 is not a positive integer.
        >>> calculate_factorial(6)
        720
        >>> calculate_factorial(4)
        24
        >>> calculate_factorial(0)
        1
        """
    if not isinstance(n, int) or n < 0:
        raise ValueError(f'calculate_factorial({n}), {n} is not a positive integer.')
    r = 1 #                                                             error (it is not 0)
    for i in range(1, n + 1): #                                         error (range from 1 to n+1!!!)
        r *= i
    return r

def calculate_sin(x, N=10):
    """calculate_sin(x, N): computes the sin of an angle with the first N terms from the Taylor's series.
    
    Args:
        x (float):  the value in sexagesimal scale, it will converted to radians.
        N (int):     the numer of terms from the Taylor's series. Default value is 10.
    Returns:
        float:   with the estimated of the sinusoidla value of the x.
    Examples:
        >>> calculate_sin(0)
        0.0
        >>> calculate_sin(90, 20)
        1.0000000000000002
        >>> calculate_sin(45, 10)
        0.7071067811865475
        """
    x = x * math.pi / 180
    s = 0.0
    for n in range(N + 1):
        s += (-1) ** n * x ** (2 * n + 1) / calculate_factorial(2 * n + 1)
    return s




def calculate_MCM(a, b):
    """calculate_MCM(a,b) computes the minimum common multiple of a and b.
    
    Args:
        a (int): the first integer.
        b (int): the second integer.
    Returns:
        int: the mcm.
    Examples:
        >>> calculate_MCM(4, 6)
        12
        >>> calculate_MCM(15, 45)
        45
        >>> calculate_MCM(12, 8)
        24
        >>> calculate_MCM(150, 340)
        5100
        """
    a, b = max(a, b), min(a, b)
    A = a
    not_found = True
    while A % b != 0:
        A += a
    return A


def calculate_ln_x_plus_1(x, N = 10):
    """calculate_ln_x_plus_1(x) computes the neperian logarithm of a float number within (-1.0, 1.0).
    
    Args:
        x (float):  the value in (-1.0, 1.0), otherwise an ValueError exception is raised.
        N (int):    the numer of terms from the Taylor's series. Default value is 10.
    Returns:
        float: the calculated value of ln(x+1)
    Exception:
        ValueError in case of x not in (-1.0, 1.0).
    Examples:
        >>> calculate_ln_x_plus_1(0.5)
        0.39346934027562475
        >>> calculate_ln_x_plus_1(-0.75, 5)
        -1.1167236328125
        >>> calculate_ln_x_plus_1(1.5)
        Traceback (most recent call last):
        ...
        ValueError: calculate_ln_x_plus_1: 1.5 not in (-1.0, 1.0) as requested.
    """
    if abs(x) >= 1:
        raise ValueError(f'calculate_ln_x_plus_1: {x} not in (-1.0, 1.0) as requested.')
    s = 0
    for n in range(1, N + 1):
        s += (-1) * (- x) ** n / calculate_factorial(n)
    return s


if __name__ == "__main__":
    import doctest

    doctest.testmod()
