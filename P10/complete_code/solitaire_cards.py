import random

# This could be done with tuples, since they will not change.
CARD_NAMES = (
    "1_of_spades",
    "2_of_spades",
    "3_of_spades",
    "4_of_spades",
    "5_of_spades",
    "1_of_hearts",
    "2_of_hearts",
    "3_of_hearts",
    "4_of_hearts",
    "5_of_hearts",
    "1_of_diamonds",
    "2_of_diamonds",
    "3_of_diamonds",
    "4_of_diamonds",
    "5_of_diamonds",
    "1_of_clubs",
    "2_of_clubs",
    "3_of_clubs",
    "4_of_clubs",
    "5_of_clubs",
)
CARD_NUMBERS = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
CARD_SUITS = (
    "spades",
    "spades",
    "spades",
    "spades",
    "spades",
    "hearts",
    "hearts",
    "hearts",
    "hearts",
    "hearts",
    "diamonds",
    "diamonds",
    "diamonds",
    "diamonds",
    "diamonds",
    "clubs",
    "clubs",
    "clubs",
    "clubs",
    "clubs",
)
CARD_COLORS = (
    "black",
    "black",
    "black",
    "black",
    "black",
    "red",
    "red",
    "red",
    "red",
    "red",
    "red",
    "red",
    "red",
    "red",
    "red",
    "black",
    "black",
    "black",
    "black",
    "black",
)
CARD_INFO = (CARD_NAMES, CARD_NUMBERS, CARD_SUITS, CARD_COLORS)

def create_shuffled_deck():
    """Receives a tuple of card names and returns a shuffled list.

    Parameters:
        card_names(tuple(str)): The tuple of cards

    Returns:
        list(str): The list of cards shuffled.
    """
    shuffled_deck = list(CARD_NAMES)
    random.shuffle(shuffled_deck)
    return shuffled_deck


def get_card_number(card_name):
    """Returns the number of the card.

    Parameters:
        card_name(str): The name of the card.

    Returns:
        int: The number of the card
    """
    index = CARD_NAMES.index(card_name)
    return CARD_NUMBERS[index]


def get_card_suit(card_name):
    """Returns the suit of the card.

    Parameters:
        card_name(str): The name of the card.

    Returns:
        str: The suit of the card
    """
    index = CARD_NAMES.index(card_name)
    return CARD_SUITS[index]


def get_card_color(card_name):
    """Returns the color of the card.

    Parameters:
        card_name(str): The name of the card.

    Returns:
        str: The color of the card
    """
    index = CARD_NAMES.index(card_name)
    return CARD_COLORS[index]
