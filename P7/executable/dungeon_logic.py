# -*- coding: utf-8 -*-

DICE_SIDES = 6
MIN_DICE_VALUE = 1
MAX_DICE_VALUE = DICE_SIDES


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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
