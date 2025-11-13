def compute_function(x_value):
    """ computes the function following the problem statement
    
    Args:
       x_value (float): the value on which the function is evaluated.
    Returns:
       float:  the outcome of the function on x_value.
    Exceptions:
       ValueError when x_value is not a positive real number.
    Examples:
    >>> compute_function(2.0)
    1.0
    >>> compute_function(5.0)
    -2.0
    >>> compute_function(3.0)
    -1.0
    """
    if type(x_value) is not float or x_value < 0.0:
        raise ValueError("compute_function only accepts positive real values.")
    if x_value < 2:
        return 0.0
    elif x_value == 2:
        return 1.0
    elif x_value < 5:
        return (x_value - 2) / (8 - 2) * 3 - 1.5
    elif x_value == 5:
        return -2.0
    else :
        return 1.5


def main():
    try:
        x = float(input("Type a POSITIVE float number, please: "))
    except ValueError as e:
        print(e)
        return
    r1 = compute_function(x)
    r2 = compute_function(5.0)
    r3 = compute_function(3.0)
    print([r1, r2, r3])


if __name__ == "__main__":
    main()
