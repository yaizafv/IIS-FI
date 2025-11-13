# -*- coding: utf-8 -*-

from random import randint

import dungeon_logic as logic

# It is a real code's quality metric is to have every block of code with
# a heading comment with the hint of what the block is intended for.


def main():
    # Print begin banner
    print("Welcome to the")
    print("""
          
    ▓█████▄ █    ██ ███▄    █  ▄████▓█████ ▒█████  ███▄    █     ▒█████   █████▒   ▓█████▄ ▒█████  ▒█████  ███▄ ▄███▓ ▐██▌  ▐██▌  ▐██▌
    ▒██▀ ██▌██  ▓██▒██ ▀█   █ ██▒ ▀█▓█   ▀▒██▒  ██▒██ ▀█   █    ▒██▒  ██▓██   ▒    ▒██▀ ██▒██▒  ██▒██▒  ██▓██▒▀█▀ ██▒ ▐██▌  ▐██▌  ▐██▌
    ░██   █▓██  ▒██▓██  ▀█ ██▒██░▄▄▄▒███  ▒██░  ██▓██  ▀█ ██▒   ▒██░  ██▒████ ░    ░██   █▒██░  ██▒██░  ██▓██    ▓██░ ▐██▌  ▐██▌  ▐██▌
    ░▓█▄   ▓▓█  ░██▓██▒  ▐▌██░▓█  ██▒▓█  ▄▒██   ██▓██▒  ▐▌██▒   ▒██   ██░▓█▒  ░    ░▓█▄   ▒██   ██▒██   ██▒██    ▒██  ▓██▒  ▓██▒  ▓██▒
    ░▒████▓▒▒█████▓▒██░   ▓██░▒▓███▀░▒████░ ████▓▒▒██░   ▓██░   ░ ████▓▒░▒█░       ░▒████▓░ ████▓▒░ ████▓▒▒██▒   ░██▒ ▒▄▄   ▒▄▄   ▒▄▄
    ▒▒▓  ▒░▒▓▒ ▒ ▒░ ▒░   ▒ ▒ ░▒   ▒░░ ▒░ ░ ▒░▒░▒░░ ▒░   ▒ ▒    ░ ▒░▒░▒░ ▒ ░        ▒▒▓  ▒░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░   ░  ░ ░▀▀▒  ░▀▀▒  ░▀▀▒
    ░ ▒  ▒░░▒░ ░ ░░ ░░   ░ ▒░ ░   ░ ░ ░  ░ ░ ▒ ▒░░ ░░   ░ ▒░     ░ ▒ ▒░ ░          ░ ▒  ▒  ░ ▒ ▒░  ░ ▒ ▒░░  ░      ░ ░  ░  ░  ░  ░  ░
    ░ ░  ░ ░░░ ░ ░   ░   ░ ░░ ░   ░   ░  ░ ░ ░ ▒    ░   ░ ░    ░ ░ ░ ▒  ░ ░        ░ ░  ░░ ░ ░ ▒ ░ ░ ░ ▒ ░      ░       ░     ░     ░
    ░      ░             ░      ░   ░  ░   ░ ░          ░        ░ ░               ░       ░ ░     ░ ░        ░    ░     ░     ░
    ░                                                                              ░
    """)

    # Main game loop
    turn = 0
    health = 100
    level = 1
    while health > 0:
        turn += 1

        print()
        print("*" * 80)
        print(f"* Turn {turn}")
        print("*" * 3)
        print()

        print("Your health is", health)
        print("Your level is", level)
        print()

        print("You found a monster in the darkness!")
        rolled_value = roll_and_show()
        monster_level, monster_health = logic.calculate_monster(rolled_value, level)
        print(f"As you approach, you see a level {monster_level} monster with {monster_health} health!")

        fight_must_go_on = True
        # Fight loop
        round = 0
        while monster_health > 0 and health > 0 and fight_must_go_on:
            round += 1

            print()
            print(f"ROUND {round}")
            print()

            print("Your health is", health)
            print("Monster's health is", monster_health)
            print()

            # Ask player for option
            option = None
            while not option:
                text = input("What do you want to do: [a]ttack or [r]un? ").lower()
                if text == "attack" or text == "a":
                    option = "fight"
                elif text == "run" or text == "r":
                    option = "run"
                else:
                    print("Invalid option. Please try again.")

            # Handle option
            print(f"You chose to {option}!")
            if option == "fight":
                hero_roll_value_1 = roll_and_show()
                hero_roll_value_2 = roll_and_show()
                hero_rolls = (hero_roll_value_1, hero_roll_value_2)
                monster_roll_value_1 = roll_and_show("The monster")
                monster_roll_value_2 = roll_and_show("The monster")
                monster_rolls = (monster_roll_value_1, monster_roll_value_2)
                new_health, new_monster_health = logic.calculate_fight_round(health, monster_health, hero_rolls, monster_rolls)
                # Worth noting: although the logic does'nt allow modifying both healths values, it is better to double check
                if health != new_health:
                    print(f"You lost {health - new_health} health!")
                if monster_health != new_monster_health:
                    print(f"The monster lost {monster_health - new_monster_health} health!")
                health = new_health
                monster_health = new_monster_health
                if monster_health <= 0:
                    print("You defeated the monster!")
                    level += level
                elif health <= 0:
                    print("You were defeated by the monster!")
            elif option == "run":
                print("You ran away!")
                fight_must_go_on = False   #break  # We can use break to make the code easier
            else:
                raise ValueError(f"Unknown option: {option}")

    # Print end banner
    print()
    print("The only way to scape is to")
    print("""
    ▓█████▄ ██▓█████  ▐██▌  ▐██▌  ▐██▌
    ▒██▀ ██▓██▓█   ▀  ▐██▌  ▐██▌  ▐██▌
    ░██   █▒██▒███    ▐██▌  ▐██▌  ▐██▌
    ░▓█▄   ░██▒▓█  ▄  ▓██▒  ▓██▒  ▓██▒
    ░▒████▓░██░▒████▒ ▒▄▄   ▒▄▄   ▒▄▄
    ▒▒▓  ▒░▓ ░░ ▒░ ░ ░▀▀▒  ░▀▀▒  ░▀▀▒
    ░ ▒  ▒ ▒ ░░ ░  ░ ░  ░  ░  ░  ░  ░
    ░ ░  ░ ▒ ░  ░       ░     ░     ░
    ░    ░    ░  ░ ░     ░     ░
    ░
    """)
    print("You reached level", level)


def roll_and_show(subject="You"):
    dice_rolled_value = randint(1, logic.DICE_SIDES)
    print(f"{subject} rolled a {dice_rolled_value}!")
    return dice_rolled_value


if __name__ == "__main__":
    main()
