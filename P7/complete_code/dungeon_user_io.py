# -*- coding: utf-8 -*-


def show_begin_banner():
    print("Welcome to the")
    # From: https://patorjk.com/software/taag/#p=testall&f=Bloody&t=Dungeon%20of%20Doom!!!
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


def show_end_banner(level):
    print()
    print("The only to scape is to")
    # From: https://patorjk.com/software/taag/#p=testall&f=Bloody&t=Die!!!
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


def show_turn(turn, health, level):
    print()
    print("*" * 80)
    print(f"* Turn {turn}")
    print("*" * 3)
    print()

    print("Your health is", health)
    print("Your level is", level)
    print()


def show_fight_round(round, health, monster_health):
    print()
    print(f"ROUND {round}")
    print()

    print("Your health is", health)
    print("Monster's health is", monster_health)
    print()


# We are using strings instead of integers!
OPTION_FIGHT = "fight"
OPTION_RUN = "run"


def ask_fight_option():
    option = None
    while not option:
        text = input("What do you want to do: [a]ttack or [r]un? ").lower()
        if text == "attack" or text == "a":
            option = OPTION_FIGHT
        elif text == "run" or text == "r":
            option = OPTION_RUN
        else:
            print("Invalid option. Please try again.")
    return option


def show_result_of_a_fight(health, new_health, monster_health, new_monster_health):
    if health != new_health:
        print(f"You lost {health - new_health} health!")
    if monster_health != new_monster_health:
        print(f"The monster lost {monster_health - new_monster_health} health!")


def show_death_message(health, monster_health):
    if monster_health <= 0:
        print("You defeated the monster!")
    elif health <= 0:
        print("You were defeated by the monster!")
    

#################################################################################################
### THIS IS FOR EXTRA 2
def ask_valid_laberinth_movement(pos, turn, max_turns, min_val, max_val):
    min_val, max_val = min(min_val, max_val), max(min_val, max_val)
    user = min_val - 1
    while user < min_val or user > max_val:
        try:
            user = int(input(f"""LABERITHN movement number {turn} out of {max_turns} for laberithn position {pos}.
                             
                             Type an integer UP (0), DOWN (1), LEFT (2), RIGHT(3): """))
        except ValueError as e:
            print(e)
            print("\nTry again!\n")
    return user

def print_current_laberinth_state(pos, length, turn, max_turns):
    print(f"\nLABERITHN movement number {turn} out of {max_turns} for laberithn position {pos} ({length} positions in this laberithn).")


def show_laberinth_result(pos, length, turn, max_turns, health, level):
    if health <= 0:
        print("\n---> You lose too much effort in getting out of the laberithn... you lose the game! <---\n")
        print("You are promoted to level", level)
    elif pos > length:
        print("\n--->You are the best navigating laberithns! You are out! <---- \n")
    elif turn > max_turns:
        print("\n--->Need navigation classes uh? You lost this test! <--- \n")
    else :
        print_current_laberinth_state(pos, length, turn, max_turns)

