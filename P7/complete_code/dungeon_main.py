# -*- coding: utf-8 -*-

from random import randint

import dungeon_logic as logic
import dungeon_user_io as user_io


def main():
    user_io.show_begin_banner()
    level = run_game_loop()
    user_io.show_end_banner(level)


def run_game_loop():
    """
    Main game loop.
    """

    turn = 0
    health = 100
    level = 1
    while health > 0:
        turn += 1
        user_io.show_turn(turn, health, level)
        health, level = handle_event(health, level)
    return level


def handle_event(health, level):
    """
    Handle the event based on the kind of event and call the appropriate solver.
    """
    kind = None                             # <------------ EXTRA 2
    while kind == None:
        value = roll_and_show()
        kind = logic.calculate_event(value)
    if kind == logic.EVENT_POTION:
        health = handle_potion(health)
    elif kind == logic.EVENT_MONSTER:
        health, level = handle_fight(health, level)
    elif kind == logic.EVENT_LABERINTH:   # <---- THIS IS FOR EXTRA 2
        health, level = handle_laberithn(health, level)
    else:
        raise ValueError(f"Unknown event kind: {kind}")
    return health, level


def handle_potion(health):
    print("You found a potion! What kind of potion is it?")
    value = roll_and_show()
    new_health = logic.calculate_potion(value, health)
    if new_health > health:
        print(f"A refreshing potion! You gained {new_health - health} health!")
    elif new_health < health:
        print(f"A poisonous potion! You lost {health - new_health} health!")
    else:  # Better to consider even impossible cases to make the code safer!
        print("The potion is empty!")
    return new_health


def handle_fight(health, level):
    """
    Fight loop
    """

    print("You found a monster in the darkness!")
    value = roll_and_show()
    monster_level, monster_health = logic.calculate_monster(value, level)
    print(f"As you approach, you see a level {monster_level} monster with {monster_health} health!")

    round = 0
    while monster_health > 0 and health > 0:
        round += 1
        user_io.show_fight_round(round, health, monster_health)
        option = user_io.ask_fight_option()
        print(f"You chose to {option}!")
        if option == user_io.OPTION_FIGHT:
            new_health, new_monster_health = run_a_fight(health, monster_health)
            # Worth noting: although the logic does'nt allow modifying both healths values, it is better to double check
            user_io.show_result_of_a_fight(health, new_health, monster_health, new_monster_health)
            health = new_health
            monster_health = new_monster_health
            if monster_health <= 0:
                level += level
            user_io.show_death_message(health, monster_health)
        elif option == user_io.OPTION_RUN:
            health, monster_health, level = handle_scape(health, monster_health, level)
            fight_must_go_on = False   #break  # We can use break to make the code easier
        else:
            raise ValueError(f"Unknown option: {option}")
    return health, level


def run_a_fight(health, monster_health):
        hero_rolled_value_1 = roll_and_show()
        hero_rolled_value_2 = roll_and_show()
        hero_rolls = (hero_rolled_value_1, hero_rolled_value_2)
        monster_rolled_value_1 = roll_and_show("The monster")
        monster_rolled_value_2 = roll_and_show("The monster")
        monster_rolls = (monster_rolled_value_1, monster_rolled_value_2)
        new_health, new_monster_health = logic.calculate_fight_round(health, monster_health, hero_rolls, monster_rolls)
        return new_health, new_monster_health


def handle_scape(health, monster_health, level):
    print("You ran away!")
    is_monster_attacking = roll_and_show("Looking forward a safe scape...")
    if is_monster_attacking > logic.SAFE_SCAPE_THRESHOLD:
        print("Glups! The monster is pursuing and attacking you!!!")
        new_health, new_monster_health = run_a_fight(health, monster_health)
        user_io.show_result_of_a_fight(health, new_health, monster_health, new_monster_health)
        health = new_health
        monster_health = new_monster_health
        if monster_health <= 0:
            level += level
    else :
        print("You scape successfully!")
    user_io.show_death_message(health, monster_health)
    return health, monster_health, level


#################################################################################################
### THIS IS FOR EXTRA 2
def handle_laberithn(health, level):
    n_o_turns = logic.calculate_player_number_of_turns(level)
    length = logic.calculate_LABERINTH_length(level)
    pos = 1
    ground_truth = None
    turn = 1
    update_pos = True
    while pos <= length and turn <= n_o_turns and health > 0:
        if update_pos:
            ground_truth = logic.obtain_a_random_LABERINTH_move()
            update_pos = False
        user_io.print_current_laberinth_state(pos, length, turn, n_o_turns)
        user_go = user_io.ask_valid_laberinth_movement(pos, turn, n_o_turns, logic.LABERINTH_MIN_MOVEMENT, logic.LABERINTH_MAX_MOVEMENT)
        penalty = logic.determine_punishment_for_the_current_movement(user_go, ground_truth)
        if penalty == 0:
            print(f"Congratulations! Direction for the position {pos} of the laberithn was correctly guessed.")
            update_pos = True
            pos += 1
        elif penalty == logic.LABERINTH_PUNISHMENT_SMALL :
            print(f"Uh-oh! Correct direction still not found. It is a matter of sense.")
        elif penalty == logic.LABERINTH_PUNISHMENT_LARGE:
            print(f"Uh-oh! Correct direction still not found. You have no idea.")
        turn += 1
        health = logic.update_hero_health(health, penalty) # health -= penalty
    if health > 0 and pos > length:
        level += 1
    user_io.show_laberinth_result(pos, length, turn, n_o_turns, health, level)
    return health, level
        



# Hey! We have named args!!!!
def roll_and_show(subject="You"):
    rolled_dice_value = randint(1, logic.DICE_SIDES)
    print(f"{subject} rolled a {rolled_dice_value}!")
    return rolled_dice_value


if __name__ == "__main__":
    main()
