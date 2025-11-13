def obtain_game_result_str(points, time):
    """Receives the points and time of a player and returns a string with the result of the game.

    Args:
        points (int): The points of the player.
        time (int): The time of the player.
    Returns:
        str: A string with the result of the game.
    Raises:
        ValueError: If points or time are negative.
    Examples:
        >>> obtain_game_result_str(1500, 80)
        'You win!'
        >>> obtain_game_result_str(5000, 100)
        'You lose!'
        >>> obtain_game_result_str(800, 20)
        'You lose!'
    """
    if points < 0 or time < 0:
        raise ValueError("Points and time must be non-negative.")

    message = ""

    if points > 1000 and time < 90:
        message = "You win!"
    else:
        message = "You lose!"

    return message


def obtain_achievements_str(points, time):
    """
    Receives the points and time of a player and returns a string with the achievements of the player.
    Args:
        points (int): The points of the player.
        time (int): The time of the player.
    Returns:
        str: A string with the achievements of the player.
    Raises:
        ValueError: If points or time are negative.
    Examples:
        >>> obtain_achievements_str(1500, 80)
        '-High Score!-High Speed!-'
        >>> obtain_achievements_str(5000, 100)
        '-High Score!-Slow but Steady!-'
        >>> obtain_achievements_str(800, 20)
        '-I just want to finish fast!-'
    """
    if points < 0 or time < 0:
        raise ValueError("Points and time must be non-negative.")

    achievements_str = ""
    if points > 5000 and time >= 90:
        achievements_str += "-Slow but Steady!-"
    if points <= 1000 and time < 30:
        achievements_str += "-I just want to finish fast!-"
    if points > 1000:
        achievements_str += "-High Score!-"
    if time < 90:
        achievements_str += "-High Speed!-"

    return achievements_str


def obtain_single_achievement_str(points, time):
    """
    Receives the points and time of a player and returns a string with the achievements of the player.
    Args:
        points (int): The points of the player.
        time (int): The time of the player.
    Returns:
        str: A string with the achievements of the player.
    Raises:
        ValueError: If points or time are negative.
    Examples:
        >>> obtain_single_achievement_str(1500, 80)
        '-High Score!-'
        >>> obtain_single_achievement_str(5000, 100)
        '-Slow but Steady!-'
        >>> obtain_single_achievement_str(800, 20)
        '-I just want to finish fast!-'
    """
    if points < 0 or time < 0:
        raise ValueError("Points and time must be non-negative.")

    achievements_str = ""

    if points > 5000 and time >= 90:
        achievements_str += "-Slow but Steady!-"
    elif points <= 1000 and time < 30:
        achievements_str += "-I just want to finish fast!-"
    elif points > 1000:
        achievements_str += "-High Score!-"
    elif time < 90:
        achievements_str += "-High Speed!-"
    else:
        achievements_str += "-No achievements-"

    return achievements_str
