import solitaire_cards

def count_pairs(card_list):
    """Counts the number of pairs in a card list.

    We consider pairs two cards with the same number in consecutive positions.

    Parameters:
        card_list(list(str)): The list of cards.

    Returns:
        int: The number of pairs found.

    Examples:
        >>> card_list = ['1_of_spades', '1_of_hearts', '1_of_diamonds', '2_of_hearts', '2_of_clubs']
        >>> count_pairs(card_list)
        3
        >>> count_pairs([])
        0
    """
    pairs_counter = 0
    for deck_index in range(len(card_list) - 1):
        card = card_list[deck_index]
        next_card = card_list[deck_index + 1]

        card_number = solitaire_cards.get_card_number(card)
        next_card_number = solitaire_cards.get_card_number(next_card)

        if card_number == next_card_number:
            pairs_counter += 1

    return pairs_counter

def create_columns(deck, column_number):
    """Creates columns from a deck

    Parameters:
        deck(list(str)): List of card names.
        column_number(int): The number of columns to create.

    Returns:
        list(list(str)): A list of lists with the columns.

    Examples:
        >>> deck = ['1_of_hearts', '1_of_diamonds', '1_of_clubs', '1_of_spades', '2_of_hearts', '2_of_diamonds', '2_of_clubs', '2_of_spades', '3_of_hearts', '3_of_diamonds', '3_of_clubs']
        >>> create_columns(deck, 3)
        [['1_of_hearts', '1_of_diamonds', '1_of_clubs', '1_of_spades'], ['2_of_hearts', '2_of_diamonds', '2_of_clubs', '2_of_spades'], ['3_of_hearts', '3_of_diamonds', '3_of_clubs']]
        >>> create_columns(deck, 0)
        Traceback (most recent call last):
        ...
        ValueError: The minimum number of columns is 1.
    """
    if column_number < 1:
        raise ValueError("The minimum number of columns is 1.")
    column_size = len(deck) // column_number

    if len(deck) % column_number != 0:
        column_size += 1

    columns = []

    for column_index in range(column_number):
        first_index = column_index * column_size
        final_index = first_index + column_size

        column = deck[first_index:final_index]

        columns.append(column)

    return columns

def _validate_list_index(list, index, error_message):
    if index < 0 or index >= len(list):
        raise ValueError(error_message)


def _validate_column_position(columns, position):
    column_index, row_index = position
    _validate_list_index(columns, column_index, "The column index does not exist.")
    _validate_list_index(
        columns[column_index], row_index, "The row index does not exist in the column."
    )

def move_card(columns, origin_position, destination_position):
    _validate_column_position(columns, origin_position)
    _validate_column_position(columns, destination_position)

    origin_column_index, origin_row_index = origin_position
    destination_column_index, destination_row_index = destination_position

    new_columns = []

    for column in columns:
        new_columns.append(column.copy())

    origin_card = new_columns[origin_column_index].pop(origin_row_index)
    new_columns[destination_column_index].insert(destination_row_index, origin_card)

    return new_columns

def count_pokers(card_list):
    """Counts the number of pokers in a card list.

    We consider pokers four cards with the same number in consecutive positions.

    Parameters:
        card_list(list(str)): The list of cards.

    Returns:
        int: The number of pokers found.

    Examples:
        >>> card_list = ['1_of_spades', '1_of_hearts', '1_of_diamonds', '1_of_clubs', '2_of_hearts', '2_of_clubs']
        >>> count_pokers(card_list)
        1
        >>> count_pokers(['1_of_spades', '1_of_hearts', '1_of_diamonds', '2_of_clubs'])
        0
        >>> count_pokers(['2_of_hearts', '2_of_clubs', '1_of_spades', '1_of_hearts', '1_of_diamonds', '1_of_clubs'])
        1
        >>> count_pokers([])
        0
    """
    card_number = len(card_list)
    pokers_counter = 0 # counts the number of pokers found
    card_numbers_checked = [] # stores the card with same numbers found in sequence
    
    # for each card in the list
    for deck_index in range(card_number):
        # we obtain its number
        current_card = card_list[deck_index]
        current_card_number = solitaire_cards.get_card_number(current_card)
        
        # If the number is not in the list, we empty the list.
        if current_card_number not in card_numbers_checked:
            card_numbers_checked = []
        
        # We add the current card number to the list
        card_numbers_checked.append(current_card_number)
        
        # If the list has reached size 4, it means the last 4 cards had the same number.
        if len(card_numbers_checked) == 4:
            # We reset it and add one to the poker counter.
            card_numbers_checked = []
            pokers_counter += 1

    return pokers_counter

def count_flush(card_list):
    """Counts the number of flushes in a card list.

    We consider flush five cards with consecutive numbers in consecutive positions.

    Parameters:
        card_list(list(str)): The list of cards.

    Returns:
        int: The number of flushes found.

    Examples:
        >>> card_list = ['1_of_spades', '2_of_hearts', '3_of_diamonds', '4_of_clubs', '5_of_hearts']
        >>> count_flush(card_list)
        1
        >>> count_flush(['1_of_spades', '2_of_hearts', '2_of_diamonds', '4_of_diamonds', '5_of_clubs'])
        0
        >>> count_flush(['1_of_spades', '2_of_hearts', '3_of_diamonds', '4_of_clubs', '5_of_hearts', '2_of_spades'])
        1
        >>> count_flush([])
        0
    """
    card_number = len(card_list)
    flush_counter = 0
    consecutive_numbers = []
    last_number = -1
    
    for deck_index in range(card_number):
        current_card = card_list[deck_index]
        current_card_number = solitaire_cards.get_card_number(current_card)
        
        # Check if current number continues the sequence
        if current_card_number != last_number + 1:
            consecutive_numbers = []
            
        consecutive_numbers.append(current_card_number)
        last_number = current_card_number

        # If we have 5 consecutive numbers, we found a flush
        if len(consecutive_numbers) == 5:
            consecutive_numbers = []
            flush_counter += 1
    
    return flush_counter


def count_color_flush(card_list):
    """Counts the number of color flushes in a card list.

    We consider color flush five cards with consecutive numbers of the same suit in consecutive positions.

    Parameters:
        card_list(list(str)): The list of cards.

    Returns:
        int: The number of color flushes found.

    Examples:
        >>> card_list = ['1_of_spades', '2_of_spades', '3_of_spades', '4_of_spades', '5_of_spades']
        >>> count_color_flush(card_list)
        1
        >>> count_color_flush(['1_of_spades', '2_of_hearts', '3_of_spades', '4_of_spades', '5_of_spades'])
        0
        >>> count_color_flush(['1_of_spades', '2_of_spades', '3_of_spades', '4_of_spades', '5_of_spades', '2_of_spades'])
        1
        >>> count_color_flush([])
        0
    """
    card_number = len(card_list)
    color_flush_counter = 0
    consecutive_numbers = []
    last_number = -1
    last_suit = None
    
    for deck_index in range(card_number):
        current_card = card_list[deck_index]
        current_card_number = solitaire_cards.get_card_number(current_card)
        current_card_suit = solitaire_cards.get_card_suit(current_card)
        
        # Check if current number continues the sequence AND has same suit
        if current_card_number != last_number + 1 or current_card_suit != last_suit:
            consecutive_numbers = []
            
        consecutive_numbers.append(current_card_number)
        last_number = current_card_number
        last_suit = current_card_suit

        # If we have 5 consecutive numbers of same suit, we found a color flush
        if len(consecutive_numbers) == 5:
            consecutive_numbers = []
            color_flush_counter += 1
    
    return color_flush_counter


def count_color(card_list):
    """Counts the number of colors in a card list.

    We consider color five consecutive cards of the same color in consecutive positions.

    Parameters:
        card_list(list(str)): The list of cards.

    Returns:
        int: The number of colors found.

    Examples:
        >>> card_list = ['1_of_spades', '5_of_clubs', '3_of_spades', '3_of_clubs', '3_of_spades']
        >>> count_color(card_list)
        1
        >>> count_color(['1_of_spades', '2_of_hearts', '3_of_spades', '4_of_clubs', '5_of_spades'])
        0
        >>> count_color(['1_of_spades', '2_of_clubs', '3_of_spades', '4_of_clubs', '5_of_spades', '2_of_clubs'])
        1
        >>> count_color([])
        0
    """
    card_number = len(card_list)
    color_counter = 0
    card_colors = []

    
    for deck_index in range(card_number):
        current_card = card_list[deck_index]
        current_card_color = solitaire_cards.get_card_color(current_card)
        
        # Check if current card has the same color as the sequence
        if current_card_color not in card_colors:
            card_colors = []
            
       
        card_colors.append(current_card_color)
        
        # If we have 5 cards of same color, we found a color
        if len(card_colors) == 5:
            card_colors = []
            color_counter += 1
    
    return color_counter

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
