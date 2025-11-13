def ask_initial_and_final_integers():
    """Asks the user to enter the initial and final numbers.

    Validates that the initial number is less than or equal to the final number.
    Continues asking until valid inputs are provided.
    Handles conversion errors when parsing input to integers.

    Returns:
        tuple: A tuple containing the initial and final numbers.
    """

    # Initialize the numbers to invalid values
    initial_number = 0
    final_number = -1

    while initial_number < final_number:
        try:
            initial_number = int(input("Enter the initial number: "))
            final_number = int(input("Enter the final number: "))

            if initial_number < final_number:
                print(f"Error: initial_number ({initial_number}) is greater than final_number ({final_number}).")

        except ValueError:
            print("Error: Please enter valid integer numbers.")

    return initial_number, final_number


def ask_integer(message):
    """Asks the user to enter a number.

    Validates that the number is an integer.
    Continues asking until a valid input is provided.
    Handles conversion errors when parsing input to integers.

    Returns:
        int: The integer entered by the user.
    """
    number = None

    while number is None:
        try:
            number = int(input(message))
        except ValueError:
            print("Error: Please enter a valid integer number.")

    return number


def ask_angle():
    """Asks the user to enter a sexagesimal angle.

    Validates that the number is an angle in [-360.0, 360.0].
    Continues asking until a valid input is provided.
    Handles conversion errors when parsing input to float.

    Returns:
        float: The angle entered by the user.
    """
    repeat = True

    while repeat:
        try:
            number = float(input("Please enter an angle in [-360.0, 360.0]: "))
        except ValueError:
            print("Error: Please enter a valid angle value.")
        if number < -360.0 or number > 360.0:
            print("\tPlease, the angle must be in [-360.0, 360.0].")
        else :
            repeat = False
    return number


def ask_float_smaller_than_1(message):
    """Asks the user to enter a float number in (1.0, 1.0).

    Validates that the number is an float value in (1.0, 1.0).
    Continues asking until a valid input is provided.
    Handles conversion errors when parsing input to float.

    Returns:
        float: The float number entered by the user.
    """
    repeat = True

    while repeat:
        try:
            number = float(input(message))
        except ValueError:
            print("Error: Please enter a valid float number.")
        if number <= -1.0 or number >= 1.0:
            print("\tPlease, the float number  must be in (-1.0, 1.0).")
        else :
            repeat = False
    return number