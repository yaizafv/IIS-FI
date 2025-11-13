"""
Cambios realizados:
- Se ha prescindido de los parámetros para las funciones ask.
    - Requerían que quien los pasase conociese todos los detalles internos de la función.
    - A menos que se vayan a usar en diversos contextos, es mejor que la función los gestione internamente.
"""

import game_logic


def ask_float_between_0_and_1():
    """Asks the user for a float number in the range [0.0, 1.0].
    If the user types a number outside the range, a 0.0 is returned.

    Returns:
        float: a value within [0.0, 1.0], or 0.0 if input is out of range.
    Raises:
        ValueError: when the user types text that cannot be converted to float.
    """
    input_text = input("Introduce a float number in [0.0, 1.0]: ")
    float_value = float(input_text)

    value_in_range = float_value >= 0.0 or float_value <= 1.0

    if not value_in_range:
        print("The introduced value is out of the range [0.0, 1.0].\nA 0.0 will be used instead.")
        float_value = 0.0

    return float_value


def ask_for_a_single_character():
    """A Question of Letters' input: requests the user for a letter.
    When longer strings are given, the letter with the minimum code is chosen.
    When an empty string is given, the blank character is returned instead.

    Args:
        msg (str): the string to prompt the user when requesting a letter.
        long_str_error (str): the message to show when the user's input is longer than a single character.
        empty_str_error (str): the message to show when the user's input is an empty string.
    Returns:
        str: a single character string.
    """
    character = input("Please introduce a single character: ")
    if len(character) > 1:
        print("The introduced text is longer than a single character.")
        print("The character with the minimum code will be used instead.")
        character = min(character)
    elif len(character) == 0:
        print("No character was introduced, so a blank space will be used instead.")
        character = " "
    return character


def ask_rock_paper_scissors():
    """Rock, Paper, Scissors input: requests the user for info for the game.

    Args:
        msg (str): message to prompt to the user.
    Returns:
        str: 'R', 'P', or 'S' (uppercase)
    Raises:
        ValueError: when the user types something that is not in {'R', 'P', 'S'} (case insensitive).
    """
    user_choice = input("Rock, Paper, Scissors: type 'R', 'P' or 'S', respectively, for choosing the desired play: ")
    user_choice = user_choice.upper()  # In case the user types lowercase letters
    if not (user_choice == "R" or user_choice == "S" or user_choice == "P"):
        raise ValueError(f"RPS input error: {user_choice} is neither (R)ock, (P)aper nor (S)cissors!")
    return user_choice


def print_dungeons_realm_result(user_choice, random_cpu_value, result):
    """Dragon's Realm: prints the result of the game.

    Args:
        user_choice (float): the value chosen by the user.
        random_cpu_value (float): the value chosen by the computer.
        result (int): the result of the game (WIN_STATE, DRAW_STATE, or LOSE_STATE).
    Returns:
        None
    """
    print(f"Dragon's Realm: You selected {user_choice} and the computer picked up {random_cpu_value}")
    if result == game_logic.WIN_STATE:
        print("Dragon's Realm: ---> you've won!")
    elif result == game_logic.DRAW_STATE:
        print("Dragon's Realm: ---> you've drawn!")
    else:
        print("Dragon's Realm: ---> you've lost!")


def print_a_question_of_letters_result(user_letter, first_letter, second_letter, result):
    """A Question of Letters: prints the result of the game.

    Args:
        user_letter (str): the user's letter in the range [a, z].
        first_letter (str): the first letter in the range [a, z].
        second_letter (str): the second letter in the range [a, z].
        result (int): the result of the game.
    Returns:
        No return value.
    """
    if result == game_logic.WIN_STATE:
        print(f"A Question of Letters: {user_letter} is actually in [{first_letter}, {second_letter}]! You've won!")
    else:
        print(f"A Question of Letters: {user_letter} is not in [{first_letter}, {second_letter}]! You've lost!")


def print_rock_paper_scissors_result(user_choice, cpu_choice, result):
    """Rock, Paper, Scissors: prints the result of the game.

    Args:
        user_choice (str): the choice made by the user ('R', 'P', or 'S').
        cpu_choice (str): the choice made by the computer ('R', 'P', or 'S').
        result (int): the result of the game (WIN_STATE, DRAW_STATE, or LOSE_STATE).
    Returns:
        None
    """
    print(f"Rock, Paper, Scissors: CPU is {cpu_choice}, you chose {user_choice}... ")
    if result == game_logic.WIN_STATE:
        print("Rock, Paper, Scissors: you've won!")
    elif result == game_logic.LOSE_STATE:
        print("Rock, Paper, Scissors: you've lost!")
    else:
        print("Rock, Paper, Scissors: you've drawn!")


def print_dungeons_result(die1, die2, die3, result):
    """Dungeons: prints the result of the game.

    Args:
        die1 (int): the value of the first die (1-6).
        die2 (int): the value of the second die (1-6).
        die3 (int): the value of the third die (1-6).
        result (int): the result of the game (WIN_STATE or LOSE_STATE).
    Returns:
        None
    """
    print(f"Dungeons: You rolled {die1}, {die2} and {die3}")
    if result == game_logic.WIN_STATE:
        print("Dungeons: Wow, this is your lucky day! Go out and live in peace!")
    else:
        print("Dungeons: HA HA HA! You are a looser!")

