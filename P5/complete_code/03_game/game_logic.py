"""
Cambios:
- Declaración de constantes para los estados de victoria, empate y derrota.
- Nombres de algunas funciones, parámetros y variables para mayor claridad.
- Aclaraciones adicionales en los docstrings.
- Modificaciones en algunos condicionales para que se alineen con la semántica del problema.

"""

WIN_STATE = 1
DRAW_STATE = 0
LOSE_STATE = -1


def solve_dragons_realm_decision(user_guess, cpu_guess):
    """Dragon's Realm guess: takes the decision on the user and cpu guesses and returns either a WIN_STATE, DRAW_STATE or LOSE_STATE.

    The user guess must be as close as possible to the cpu guess to win.

    Args:
        user_guess (float): the user's real value in the interval [0.0, 1.0].
        cpu_guess (float): the cpu guess as a real value in [0.0, 1.0].
    Returns:
        int: WIN_STATE (1) when the user wins (difference < 0.125),
             DRAW_STATE (0) when there is a draw (difference < 0.2 and >= 0.125),
             LOSE_STATE (-1) when the user loses (difference >= 0.2).
    Examples:
        >>> solve_dragons_realm_decision(0.45, 0.5)
        1
        >>> solve_dragons_realm_decision(0.65, 0.5)
        0
        >>> solve_dragons_realm_decision(0.75, 0.5)
        -1

    """
    difference = abs(user_guess - cpu_guess)

    if difference < 0.125:
        result = WIN_STATE
    elif difference < 0.2:
        result = DRAW_STATE
    else:
        result = LOSE_STATE

    return result


def solve_a_question_of_letters(user_letter, first_letter, second_letter):
    """A Question of Letters' Takes a letter from the user and checks if it is between two letters.
    If the letter is between the two letters, the user wins. Otherwise, the user loses.
    There is no draw state in this game.

    Args:
        user_letter (str): the user's letter in the range [a, z].
        first_letter (str): the first letter in the range [a, z].
        second_letter (str): the second letter in the range [a, z].
    Returns:
        int: WIN_STATE when the user wins (user_letter is between first_letter and second_letter inclusive),
             LOSE_STATE when the user loses. No draw is possible.
    Examples:
        >>> solve_a_question_of_letters("d", "b", "s")
        1
        >>> solve_a_question_of_letters("a", "b", "s")
        -1
    """
    victory = user_letter >= first_letter and user_letter <= second_letter

    if victory:
        result = WIN_STATE
    else:
        result = LOSE_STATE

    return result


def solve_rock_paper_scissors(user_choice, cpu_choice):
    """Rock, Paper, Scissors' solution: takes the user and cpu choices and returns a WIN, LOSE or DRAW state.
    Rock (r) beats Scissors (s), Scissors (s) beats Paper (p), and Paper (p) beats Rock (r).

    Args:
        user_choice (str): the user's choice in ['R', 'P', 'S'].
        cpu_choice (str): the computer's choice in ['R', 'P', 'S'].
    Returns:
        int: WIN_STATE when the user wins,
             DRAW_STATE when there is a draw (same choices),
             LOSE_STATE  when the user loses.
    Examples:
        >>> solve_rock_paper_scissors("R", "S")
        1
        >>> solve_rock_paper_scissors("R", "P")
        -1
        >>> solve_rock_paper_scissors("R", "R")
        0
    """

    if user_choice == cpu_choice:
        return DRAW_STATE

    user_rock_cpu_scissors = user_choice == "R" and cpu_choice == "S"
    user_paper_cpu_rock = user_choice == "P" and cpu_choice == "R"
    user_scissors_cpu_paper = user_choice == "S" and cpu_choice == "P"

    if user_rock_cpu_scissors or user_paper_cpu_rock or user_scissors_cpu_paper:
        result = WIN_STATE
    else:
        result = LOSE_STATE

    return result


def solve_dungeons(die1, die2, die3):
    """Dungeons' solution: Receives three dice values and checks if their sum is even or if the sum is odd and the three dice are odd.
    If any of the conditions are met, the user wins. Otherwise, the user loses.
    There is no draw state in this game.

    Args:
        die1 (int): the first die value (1-6).
        die2 (int): the second die value (1-6).
        die3 (int): the third die value (1-6).
    Returns:
        int: WIN_STATE (1) when the user wins (both dice are even and their sum is even),
             LOSE_STATE (-1) when the user loses. No draw is possible.
    Examples:
        >>> solve_dungeons(2, 4, 2)  # The sum (8) is even
        1
        >>> solve_dungeons(2, 3, 4)  # Sum is odd, but only one odd die
        -1
        >>> solve_dungeons(1, 3, 3)  # First odd, all three dice are odd
        1
    """
    is_die1_even = die1 % 2 == 0
    is_die2_even = die2 % 2 == 0
    is_die3_even = die3 % 2 == 0
    three_dice_are_odd = is_die1_even and is_die2_even and is_die3_even
    is_sum_even = (die1 + die2 + die3) % 2 == 0
    is_sum_and_3dice_odd = (die1 + die2 + die3) % 2 != 0 and three_dice_are_odd
    victory = is_sum_even or is_sum_and_3dice_odd

    if victory:
        result = WIN_STATE
    else:
        result = LOSE_STATE

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
