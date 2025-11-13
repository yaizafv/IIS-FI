import calculator_logic as calculator
import calculator_user_io as user_io

SUMMATORY_OPTION = 0
COUNT_NUMBERS_OPTION = 1
MCD_OPTION = 2
SIN_OPTION = 3
MCM_OPTION = 4
LN1_OPTION = 5
EXIT_OPTION = -1
NO_OPTION = -2

MIN_OPTION_VALUE = EXIT_OPTION
MAX_OPTION_VALUE = LN1_OPTION


def show_menu():
    """Displays the menu options to the user."""
    print("Menu:")
    print(f"{SUMMATORY_OPTION}. Sum")
    print(f"{COUNT_NUMBERS_OPTION}. Count")
    print(f"{MCD_OPTION}. MCD")
    print(f"{SIN_OPTION}. Sin")
    print(f"{MCM_OPTION}. MCM")
    print(f"{LN1_OPTION}. ln(1+x)")
    print(f"{EXIT_OPTION}. Exit")


def ask_menu_option():
    """Asks the user to select a menu option.

    Returns:
        int: The selected menu option.
    """

    option = int(input("Select an option: "))
    if option < MIN_OPTION_VALUE or option > MAX_OPTION_VALUE:
        raise ValueError(f"Option {option} is not valid. Please select a number between {MIN_OPTION_VALUE} and {MAX_OPTION_VALUE}.")

    return option


def run_summatory():
    """Runs the summatory function."""
    initial_number, final_number = user_io.ask_initial_and_final_integers()
    result = calculator.calculate_summatory(initial_number, final_number)
    print(f"The sum of numbers from {initial_number} to {final_number} is: {result}")


def run_count_numbers_ascending():
    """Runs the count function."""
    initial_number, final_number = user_io.ask_initial_and_final_integers()
    result = calculator.count_numbers_ascending(initial_number, final_number)
    print(f"The numbers from {initial_number} to {final_number} are: {result}")


def run_mcd():
    """Runs the MCD function."""
    dividend = user_io.ask_integer("Please enter the dividend:")
    divisor = user_io.ask_integer("Please enter the divisor: ")
    result = calculator.calculate_mcd(dividend, divisor)
    print(f"The MCD of {dividend} and {divisor} is: {result}")


def run_sin():
    """Runs the SIN function."""
    angle = user_io.ask_angle()
    N = user_io.ask_integer("Please enter the number of terms in the series: ")
    result = calculator.calculate_sin(angle, N)
    print(f"The SIN of {angle} with {N} terms is: {result}")


def run_mcm():
    """Runs the MCM function."""
    first = user_io.ask_integer("Please enter the first integer:")
    second = user_io.ask_integer("Please enter the second integer: ")
    result = calculator.calculate_MCM(first, second)
    print(f"The MCD of {first} and {second} is: {result}")

def run_ln_x_plus_1():
    """Runs the MCM function."""
    x = user_io.ask_float_smaller_than_1("Please enter a float value in (-1.0, 1.0): ")
    N = user_io.ask_integer("Please enter the number of terms: ")
    result = calculator.calculate_ln_x_plus_1(x, N)
    print(f"The ln of 1+{x} with {N} terms is: {result}")


def handle_option(option):
    """Dispatches the selected option to the corresponding function.

    Args:
        option (int): The selected menu option.
    """
    if option == SUMMATORY_OPTION:
        run_summatory()
    elif option == COUNT_NUMBERS_OPTION:
        run_count_numbers_ascending()
    elif option == MCD_OPTION:
        run_mcd()
    elif option == SIN_OPTION:
        run_sin()
    elif option == MCM_OPTION:
        run_mcm()
    elif option == LN1_OPTION:
        run_ln_x_plus_1()
    elif option == EXIT_OPTION:
        print("Exiting the program.")
    else:
        print(f"Option {option} is not valid. It must be {MIN_OPTION_VALUE} and {MAX_OPTION_VALUE}.")


def main():
    option = NO_OPTION

    while option != EXIT_OPTION:
        show_menu()
        option = ask_menu_option()
        handle_option(option)


if __name__ == "__main__":
    main()
