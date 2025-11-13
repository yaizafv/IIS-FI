import random

import game_logic
import game_user_io as user_io

LETTERS_STATE = "LETTERS"
DUNGEONS_STATE = "DUNGEONS"
ROCK_PAPER_SCISSORS_STATE = "RPS"
FINISH_WINNING = "WIN"
FINISH_LOSING = "LOSE"


def run_dragons_realm():
    """Dragon's Realm: performs the game of Dragon's Realm. To do so, requests the user for info, generates the computer go, etc.

    Returns:
        int: GAME_WIN (1) when the user wins, GAME_DRAW (0) when there is a draw, GAME_LOSE (-1) when the user loses.
    """
    print("##################################################################")
    print("Dragon's Realm!")
    random_cpu_value = random.uniform(0.0, 1.0)
    try:
        user_choice = user_io.ask_float_between_0_and_1()
    except ValueError:
        print("Dragon's Realm: You introduce an invalid value so we will use -10.0 as the user's input! You will lose the game!")
        user_choice = -10

    result = game_logic.solve_dragons_realm_decision(user_choice, random_cpu_value)
    user_io.print_dungeons_realm_result(user_choice, random_cpu_value, result)
    return result


def run_a_question_of_letters():
    """A Question of Letters: performs the game of a question of letters. To do so, requests the user for info, generates the computer go, etc.

    Returns:
        int: GAME_WIN (1) when the user wins, GAME_LOSE (-1) when the user loses. No draw is possible.
    """
    print("##################################################################")
    print("A Question of Letters!")
    user_letter = user_io.ask_for_a_single_character()
    letter1 = random.randint(ord("a"), ord("z"))
    letter2 = random.randint(ord("a"), ord("z"))

    first_letter = chr(min(letter1, letter2))
    second_letter = chr(max(letter1, letter2))

    result = game_logic.solve_a_question_of_letters(user_letter, first_letter, second_letter)
    user_io.print_a_question_of_letters_result(user_letter, first_letter, second_letter, result)
    return result


def get_random_rock_paper_scissors_choice():
    """Generates a random choice for Rock, Paper, Scissors.

    Returns:
        str: 'R', 'P', or 'S' (uppercase)
    """
    cpu_choice_int = random.randint(0, 2)
    ROCK_SELECTED = 0
    PAPER_SELECTED = 1
    SCISSORS_SELECTED = 2
    if cpu_choice_int == ROCK_SELECTED:
        cpu_choice = "R"
    elif cpu_choice_int == PAPER_SELECTED:
        cpu_choice = "P"
    elif cpu_choice_int == SCISSORS_SELECTED:
        cpu_choice = "S"
    else:
        raise ValueError(f"RPS input error: {cpu_choice_int} is not a valid choice!")

    return cpu_choice


def run_rock_paper_scissors():
    """Rock, Paper, Scissors: performs the game of the Rock, Paper, Scissors. To do so, requests the user for info, generates the computer go, etc.

    Returns:
        int: GAME_WIN (1) when the user wins, GAME_LOSE (-1) when the user loses or draws.
              Draws are treated as losses in this implementation.
    """
    print("##################################################################")
    print("Rock-Paper-Scissors!")
    cpu_choice = get_random_rock_paper_scissors_choice()

    try:
        user_choice = user_io.ask_rock_paper_scissors()
    except ValueError:
        print("You introduce an invalid value so you lose the game!")
        return game_logic.LOSE_STATE

    result = game_logic.solve_rock_paper_scissors(user_choice, cpu_choice)
    user_io.print_rock_paper_scissors_result(user_choice, cpu_choice, result)
    return result


def run_dungeons():
    """Dungeons: performs the dilemma to get out of the dungeons or to die...

    Returns:
        int: GAME_WIN (1) when the user wins, GAME_LOSE (-1) when the user loses. No draw is possible.
    """
    print("##################################################################")
    print("Dungeons!")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    result = game_logic.solve_dungeons(die1, die2, die3)
    user_io.print_dungeons_result(die1, die2, die3, result)
    return result


def main():
    print("Game Festival: Let's start with the first game!")
    result = run_dragons_realm()
    if result == game_logic.WIN_STATE:
        state = LETTERS_STATE
    elif result == game_logic.DRAW_STATE:
        state = DUNGEONS_STATE
    else:
        state = FINISH_LOSING

    if state == LETTERS_STATE:
        print("Game Festival: You move forward! Go ahead with the next game!")
        result = run_a_question_of_letters()
        if result == game_logic.WIN_STATE:
            state = ROCK_PAPER_SCISSORS_STATE
        else:
            state = DUNGEONS_STATE

    if state == DUNGEONS_STATE:
        print("Game Festival: You move backwards! Let's see if you can escape from this game!")
        result = run_dungeons()
        if result == game_logic.WIN_STATE:
            state = ROCK_PAPER_SCISSORS_STATE
            print("Dungeons: Wow, this is your lucky day! Go out and live in peace!")
        else:
            state = FINISH_LOSING
            print("Dungeons: HA HA HA! You are a looser!")

    if state == ROCK_PAPER_SCISSORS_STATE:
        print("Game Festival: You move forward! Go ahead with the next game!")
        result = run_rock_paper_scissors()
        if result == game_logic.WIN_STATE:
            state = FINISH_WINNING
        else:
            state = FINISH_LOSING

    print("##################################################################")
    if state == FINISH_WINNING:
        print("Game Festival: you win! You're a champion!")
    elif state == FINISH_LOSING:
        print("Game Festival: you lost! Sorry Chap!")
    else:
        print("Game Festival: nobody knows what had happened!")


if __name__ == "__main__":
    main()
