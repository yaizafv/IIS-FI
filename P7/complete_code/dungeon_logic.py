# -*- coding: utf-8 -*-
import random

DICE_SIDES = 6
MIN_DICE_VALUE = 1
MAX_DICE_VALUE = DICE_SIDES

SAFE_SCAPE_THRESHOLD = 4

EVENT_POTION = 1
EVENT_MONSTER = 2
EVENT_LABERINTH = 3 # <---- THIS IS FOR EXTRA 2

def calculate_event(value):
    """
    Decides which event has been generated.

    Args:
        value (int): the outcome of a die doll.
    Returns:
        int with the possible event constant.
    Exceptions:
        ValueError due to the call to validate_roll.
    Examples:
        >>> calculate_event(1)
        1
        >>> calculate_event(2)
        2
        >>> calculate_event(3)
        3
    """
    validate_roll(value, "event kind")
    
    # This is a design decision, with hardcoded options.
    if value == 1:
        return EVENT_POTION
    elif value == 2:
        return EVENT_MONSTER
    elif value == 3:   # <---- THIS IS FOR EXTRA 2
        return EVENT_LABERINTH
    else :
        return None # EVENT_MONSTER


# Some constants for the calculate_potion function
POTION_THRESHOLD = 3  # Chance of 50% in a 6 sided dice
POTION_DAMAGE = 10
POTION_CURE = 10


def calculate_potion(kind, health):
    """
    Calculate the effect of a potion.

    Args:
        kind (int): The kind of potion.
        health (int): The current health of the player.
    Returns:
        int: The new health of the player.
    Raises:
        ValueError: From validate_roll.
    Example:
        >>> calculate_potion(POTION_THRESHOLD - 1, 50)
        40
        >>> calculate_potion(POTION_THRESHOLD, 50)
        40
        >>> calculate_potion(POTION_THRESHOLD + 1, 50)
        60
        >>> calculate_potion(POTION_THRESHOLD + 1, 100)
        100
        >>> calculate_potion(POTION_THRESHOLD - 1, 0)
        0
        >>> calculate_potion(MIN_DICE_VALUE - 1, 50)
        Traceback (most recent call last):
            ...
        ValueError: potion kind must be between 1 and 6
        >>> calculate_potion(MAX_DICE_VALUE + 1, 50)
        Traceback (most recent call last):
            ...
        ValueError: potion kind must be between 1 and 6
    """

    validate_roll(kind, "potion kind")

    if kind <= POTION_THRESHOLD:
        amount = -POTION_DAMAGE
    else:
        amount = POTION_CURE
    return update_hero_health(health, amount)



MONSTER_HEALTH_MULTIPLIER = 10

def calculate_monster(kind, level):
    """
    Calculate the monster's level and health.

    Args:
        kind (int): The kind of monster.
        level (int): The current level of the player.
    Returns:
        tuple: The level and health of the monster.
    Raises:
        ValueError: From validate_roll.
    Example:
        >>> calculate_monster(1, 10)
        (8, 80)
        >>> calculate_monster(2, 10)
        (9, 90)
        >>> calculate_monster(3, 10)
        (10, 100)
        >>> calculate_monster(4, 10)
        (11, 110)
        >>> calculate_monster(5, 10)
        (12, 120)
        >>> calculate_monster(6, 10)
        (13, 130)
        >>> calculate_monster(0, 10)
        Traceback (most recent call last):
            ...
        ValueError: monster kind must be between 1 and 6
        >>> calculate_monster(7, 10)
        Traceback (most recent call last):
            ...
        ValueError: monster kind must be between 1 and 6
        >>> calculate_monster(1, 0)
        (1, 10)
    """

    validate_roll(kind, "monster kind")

    monster_level = level + kind - DICE_SIDES // 2
    if monster_level < 1:
        monster_level = 1
    monster_health = monster_level * MONSTER_HEALTH_MULTIPLIER
    return monster_level, monster_health


def calculate_fight_round(health, monster_health, hero_rolls, monster_rolls):
    """
    Calculate the effect of a fight round.

    Args:
        health (int): The current health of the player.
        monster_health (int): The current health of the monster.
        hero_rolls (list): The rolls of the player.
        monster_rolls (list): The rolls of the monster.
    Returns:
        tuple: The new health of the player and the monster.
    Example:
        >>> calculate_fight_round(100, 100, [1, 2], [3, 4])
        (93, 100)
        >>> calculate_fight_round(100, 100, [3, 4], [1, 2])
        (100, 30)
        >>> calculate_fight_round(100, 100, [1, 2], [1, 2])
        (100, 100)
    """

    validate_rolls(hero_rolls, "hero rolls")
    validate_rolls(monster_rolls, "monster roll")

    hero_damage = sum(hero_rolls)
    monster_damage = sum(monster_rolls)
    if hero_damage > monster_damage:
        hero_damage *= 10
        monster_health = update_monster_health(monster_health, -hero_damage)
    elif monster_damage > hero_damage:
        health = update_hero_health(health, -monster_damage)
    return health, monster_health


def validate_rolls(values, domain):
    validate_roll(values[0], domain)
    validate_roll(values[1], domain)
    # Once we study lists and looping on them, this function must
    # have a code like the following:
    # 
    # for value in values:
    #     validate_roll(value, domain)


def validate_roll(value, domain):
    if value < MIN_DICE_VALUE or value > MAX_DICE_VALUE:
        raise ValueError(f"{domain} must be between {MIN_DICE_VALUE} and {MAX_DICE_VALUE}")


# Sometimes, constants are placed near their main use, making easier the manteinance of the code
HERO_MIN_HEALTH = 0
HERO_MAX_HEALTH = 100


def update_hero_health(health, amount):
    # The same update function is used, but with specific parameters for the player.
    return update_health(health, amount, HERO_MIN_HEALTH, HERO_MAX_HEALTH)


def update_monster_health(health, amount):
    # The same update function is used, but with specific parameters for the player.
    #  In this case, None is used as a discriminator.
    return update_health(health, amount, HERO_MIN_HEALTH, None)


def update_health(health, amount, min_value, max_value):
    """
    Update the health of the player or monster.

    Args:
        health (int): The current health of the player or monster.
        amount (int): The amount to add to the health.
        min_value (int): The minimum value for the health.
        max_value (int): The maximum value for the health.
    Returns:
        int: The new health of the player or monster.
    Example:
        >>> update_health(50, -10, 0, 100)
        40
        >>> update_health(50, 10, 0, 100)
        60
        >>> update_health(50, -60, 0, 100)
        0
        >>> update_health(50, 60, 0, 100)
        100
    """
    if max_value != None and health + amount > max_value:
        return max_value
    if health + amount < min_value:
        return min_value
    return health + amount

#################################################################################################
### THIS IS FOR EXTRA 2
LABERINTH_MIN_TURNS = 5
LABERINTH_MAX_TURNS = 20
LABERINTH_MIN_LEVEL = 1
LABERINTH_MAX_LEVEL  =24
LABERINTH_MIN_LENGTH = 2
LABERINTH_MAX_LENGTH = 8
def calculate_player_number_of_turns(level):
    """
    Determines the maximum number a player has.
    Limits are:
    * LABERINTH_MIN_TURNS to LABERINTH_MAX_TURNS for the number of turns.
    * Corresponding to LABERINTH_MIN_LEVEL and LABERINTH_MAX_LEVEL, correspondingly. 
    A linear correspondence is established to compute the number of turns.
    
    Args:
        level (int):  the level the game is at.
    Returns:
        int with the number of turns.
    Examples:
        >>> calculate_player_number_of_turns(1)
        5
        >>> calculate_player_number_of_turns(10)
        11
        >>> calculate_player_number_of_turns(100)
        20
        """
    noturns = round((LABERINTH_MAX_TURNS - LABERINTH_MIN_TURNS) * (level - LABERINTH_MIN_LEVEL) / (LABERINTH_MAX_LEVEL - LABERINTH_MIN_LEVEL) + LABERINTH_MIN_TURNS)
    noturns = max(LABERINTH_MIN_TURNS, noturns)
    noturns = min(LABERINTH_MAX_TURNS, noturns)
    return noturns

def calculate_LABERINTH_length(level):
    """
    Determines the length of the laberinth according to the level.
    Limits are:
    * LABERINTH_MIN_LENGTH to LABERINTH_MAX_LENGTH for the length.
    * Corresponding to LABERINTH_MIN_LEVEL and LABERINTH_MAX_LEVEL, correspondingly. 
    A linear correspondence is established to compute the length.
    
    Args:
        level (int):  the level the game is at.
    Returns:
        int with the length of the laberinth.
    Examples:
        >>> calculate_LABERINTH_length(1)
        2
        >>> calculate_LABERINTH_length(10)
        4
        >>> calculate_LABERINTH_length(100)
        8
        """
    length = round((LABERINTH_MAX_LENGTH - LABERINTH_MIN_LENGTH) * (level - LABERINTH_MIN_LEVEL) / (LABERINTH_MAX_LEVEL - LABERINTH_MIN_LEVEL) + LABERINTH_MIN_LENGTH)
    length = max(LABERINTH_MIN_LENGTH, length)
    length = min(LABERINTH_MAX_LENGTH, length)
    return length

LABERINTH_UP = 0
LABERINTH_DOWN = 1
LABERINTH_LEFT = 2
LABERINTH_RIGHT = 3
LABERINTH_MIN_MOVEMENT = min(LABERINTH_UP, LABERINTH_DOWN, LABERINTH_LEFT, LABERINTH_RIGHT)
LABERINTH_MAX_MOVEMENT = max(LABERINTH_UP, LABERINTH_DOWN, LABERINTH_LEFT, LABERINTH_RIGHT)

def assert_is_a_valid_movement(move):
    """
    Analyses whether the given movement is valir or not.
    Valid movements: LABERINTH_UP (0), LABERINTH_DOWN (1), LABERINTH_LEFT (2), LABERINTH_RIGHT (3).

    Args:
        move (int):   the movement to check.
    Returns:
        bool with the validation result.
    Exception:
        ValueError when the movement is not valid.
    Examples:
        >>> assert_is_a_valid_movement(1)
        True
        >>> assert_is_a_valid_movement(2)
        True
    """
    ret = LABERINTH_MIN_MOVEMENT <= move <= LABERINTH_MAX_MOVEMENT
    if not ret:
        raise ValueError(f"LABERINTH: Movement {move} is not in [{LABERINTH_MIN_MOVEMENT}, {LABERINTH_MAX_MOVEMENT}]!")
    return True

LABERINTH_UP_STR = "UP"
LABERINTH_DOWN_STR = "DOWN"
LABERINTH_LEFT_STR = "LEFT"
LABERINTH_RIGHT_STR = "RIGHT"
LABERINTH_DEFAULT_STR = ""
def get_direction_string(move):
    """
    Translates the integer with the movement to a str that represents it in human standards.
    
    Args:
        move (int) a movement.
    Returns:
        str with the standard str.
    Examples:
        >>> get_direction_string(0)
        'UP'
        >>> get_direction_string(1)
        'DOWN'
        """
    assert_is_a_valid_movement(move)
    if move == LABERINTH_UP:
        return LABERINTH_UP_STR
    elif move == LABERINTH_DOWN:
        return LABERINTH_DOWN_STR
    elif move == LABERINTH_LEFT:
        return LABERINTH_LEFT_STR
    elif move == LABERINTH_RIGHT:
        return LABERINTH_RIGHT_STR
    else :
        return LABERINTH_DEFAULT_STR
    
def obtain_a_random_LABERINTH_move(subject = "LABERINTH next direction"):
    """
    Returns one of the possible movements: UP (0), DOWN (1), LEFT (2), or RIGHT (3).
    
    Args:
        subject (str):   a message to identify who is using the function during the inner printing.
    Returns:
        int with the random movement LABERINTH_UP (0), LABERINTH_DOWN (1), LABERINTH_LEFT (2), LABERINTH_RIGHT (3).
    Examples:
        > >> obtain_a_random_LABERINTH_move()  # not intended to be used with doctest as long is a random guess.
        0
        > >> obtain_a_random_LABERINTH_move()  # not intended to be used with doctest as long is a random guess.
        3
        """
    ret = random.randint(LABERINTH_MIN_MOVEMENT, LABERINTH_MAX_MOVEMENT)
    print(f"Obtaining the {subject}, direction {get_direction_string(ret)} chosen.")
    return ret

LABERINTH_PUNISHMENT_SMALL = 5
LABERINTH_PUNISHMENT_LARGE = 10

def determine_punishment_for_the_current_movement(move, correct):
    """
    Calculates the punishment for the player's movement and the correct direction.
    
    Args:
        move (int):   the player's movement.
        correct (int):  the current correct direction.
    Return:
        int with the punishment to apply to the user for his/her guess.
    Examples:
        >>> determine_punishment_for_the_current_movement(0, 1)
        5
        >>> determine_punishment_for_the_current_movement(0, 3)
        10
        >>> determine_punishment_for_the_current_movement(0, 0)
        0
        """
    punish = 0
    if move == LABERINTH_DOWN or move == LABERINTH_UP:
        if move == correct:
            punish = 0
        elif correct == LABERINTH_DOWN or correct == LABERINTH_UP:
            punish = LABERINTH_PUNISHMENT_SMALL
        else :
            punish = LABERINTH_PUNISHMENT_LARGE
    elif move == LABERINTH_LEFT or move == LABERINTH_RIGHT:
        if move == correct:
            punish = 0
        elif correct == LABERINTH_LEFT or correct == LABERINTH_RIGHT:
            punish = LABERINTH_PUNISHMENT_SMALL
        else :
            punish = LABERINTH_PUNISHMENT_LARGE
    else :
        raise ValueError(f"LABERINTH: {move} is not within limits!")
    return punish



if __name__ == "__main__":
    import doctest

    doctest.testmod()
