import math  #                                                        error (math was not included)

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

def calculate_cosine(x, N = 10):
    """ cosine(x): returns the value of this function computed with the Taylor's series.
    
    Args:
        x(float): the angle in sexagesimal degrees.
        N(int): the number of terms in the series to consider. Default value is 10.
    Returns:
        float: with the computed cosine.
    Examples:
        >>> calculate_cosine(45)
        0.7071067811865475
        >>> calculate_cosine(45, 2)
        0.707429206709773
    """
    x = x * math.pi / 180 # translating the angle to radians
    r = 0
    for i in range(0, N + 1):
        r += (-1) ** i * x ** (2 * i) / calculate_factorial(2 * i)  #   error ( (-1) ** i; factorial of 2 * i)
    return r

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
