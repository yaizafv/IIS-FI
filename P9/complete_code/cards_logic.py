def add_card(card_list, card):
    """Adds a card to a list.

    Parameters:
        card_list(list(str)): The list to add the card.
        card: The card to add.

    Returns:
        list(str): The updated list.

    Examples:
        >>> card_list = ['diamonds', 'hearts']
        >>> add_card(card_list, 'spades')
        ['diamonds', 'hearts', 'spades']
        >>> card_list
        ['diamonds', 'hearts']
    """
    new_card_list = card_list.copy()
    new_card_list.append(card)
    return new_card_list


def remove_card(card_list, card):
    """Removes a card to a list.

    Parameters:
        card_list(list(str)): The list to remove the card.
        card: The card to remove.

    Returns:
        list(str): The updated list.

    Examples:
        >>> card_list = ['diamonds', 'hearts']
        >>> remove_card(card_list, 'hearts')
        ['diamonds']
        >>> card_list
        ['diamonds', 'hearts']
        >>> remove_card(card_list, 'potatoes')
        Traceback (most recent call last):
        ...
        ValueError: potatoes is not in the card list.
    """
    if card not in card_list:
        raise ValueError(f"{card} is not in the card list.")
    new_card_list = card_list.copy()
    new_card_list.remove(card)
    return new_card_list


def count_card_occurrences(card_list, card_to_count):
    """Counts the number of cards of a type in a list.

    Parameters:
        card_list(list(str)): The list to traverse
        card_to_count: The card to count.

    Returns:
        int: The number of cards found.

    Examples:
        >>> card_list = ['diamonds', 'hearts', 'spades', 'diamonds']
        >>> count_card_occurrences(card_list, 'diamonds')
        2
        >>> count_card_occurrences(card_list, 'clubs')
        0
    """
    counter = 0
    for card in card_list:
        if card == card_to_count:
            counter += 1

    return counter

def swap_card_positions(card_list, index_1, index_2):
    """Swap the positions of two cards in the list.

    Parameters:
        card_list(list(str)): The list of cards.
        index_1(int): First index to swap.
        index_2(int): Second index to swap.

    Returns:
        list(str): A new list with the indexes swapped.

    Examples:
        >>> card_list = ['spades', 'hearts', 'clubs', 'diamonds']
        >>> swap_card_positions(card_list, 0, 3)
        ['diamonds', 'hearts', 'clubs', 'spades']
        >>> card_list
        ['spades', 'hearts', 'clubs', 'diamonds']
        >>> swap_card_positions(card_list, 0, 5)
        Traceback (most recent call last):
        ...
        ValueError: Index does not exist in list.
    """
    if (
        index_1 < 0
        or index_2 < 0
        or index_1 > len(card_list)
        or index_2 > len(card_list)
    ):
        raise ValueError("Index does not exist in list.")

    new_card_list = card_list.copy()
    card_1 = card_list[index_1]
    card_2 = card_list[index_2]

    new_card_list[index_1] = card_2
    new_card_list[index_2] = card_1

    return new_card_list

def reposition_card(card_list, card, index):
    """Receives a list, a card name, and an index and repositions the card.

    Parameters:
        card_list(list(str)): The card list.
        card(str): The card name to reposition.
        index(int): The new position for the card.

    Returns:
        list(str): A new card list with the card repositioned.

    Examples:
        >>> card_list = ['hearts', 'spades', 'clubs']
        >>> reposition_card(card_list, 'spades', 0)
        ['spades', 'hearts', 'clubs']
        >>> card_list
        ['hearts', 'spades', 'clubs']
        >>> reposition_card(card_list, 'spades', 3)
        Traceback (most recent call last):
        ...
        ValueError: Introduced index out of bounds.
        >>> reposition_card(card_list, 'potatoes', 0)
        Traceback (most recent call last):
        ...
        ValueError: The card does not exist.
    """
    if index < 0 or index >= len(card_list):
        raise ValueError("Introduced index out of bounds.")

    if card not in card_list:
        raise ValueError("The card does not exist.")

    new_card_list = card_list.copy()
    original_card_index = new_card_list.index(card)
    original_card = new_card_list.pop(original_card_index)
    new_card_list.insert(index, original_card)
    return new_card_list


def cut_card_list_in_two(card_list):
    """Cuts the card_list in two and swaps the order of the two blocks.

    Paramters:
        card_list(list(str)): The cards to cut.

    Returns:
        list(str): A new card list after being cut in half and reordered.

    Examples:
        >>> card_list = ['hearts', 'hearts', 'spades', 'spades', 'spades']
        >>> cut_card_list_in_two(card_list)
        ['spades', 'spades', 'spades', 'hearts', 'hearts']
        >>> card_list
        ['hearts', 'hearts', 'spades', 'spades', 'spades']
        >>> cut_card_list_in_two([])
        []
        >>> cut_card_list_in_two(['hearts'])
        ['hearts']

    """
    # Old version of the code:
    # cut_position = len(card_list) // 2
    # block_1 = card_list[:cut_position]
    # block_2 = card_list[cut_position:]
    # new_card_list = block_2 + block_1
    
    # New version of the code using cut_cards function:
    new_card_list = cut_cards(card_list, 2)

    return new_card_list

def count_pairs(card_list):
    """Counts the number of consecutive pairs of the same card in a list.
    
    Two consecutive cards of the same kind form a pair. Each card can only 
    belong to a single pair, so overlapping pairs are not counted.
    
    Parameters:
        card_list(list(str)): The list of cards to analyze.
        
    Returns:
        int: The number of pairs found.
        
    Examples:
        >>> count_pairs(['hearts', 'hearts', 'spades', 'spades'])
        2
        >>> count_pairs(['hearts', 'hearts', 'hearts', 'spades'])
        1
        >>> count_pairs(['hearts', 'hearts', 'hearts', 'hearts'])
        2
        >>> count_pairs(['hearts', 'spades', 'hearts', 'hearts'])
        1
        >>> count_pairs(['hearts', 'spades', 'clubs', 'diamonds'])
        0
        >>> count_pairs([])
        0
        >>> count_pairs(['hearts'])
        0
    """
    card_number = len(card_list)
    
    if card_number < 2:
        return 0
    
    pairs = 0
    pair_in_last_iteration = False
    card_number = len(card_list)
    
    for i in range(0, card_number):
        if pair_in_last_iteration:
            pair_in_last_iteration = False
            continue
        
        if i + 1 < card_number and card_list[i] == card_list[i + 1]:
            pairs += 1
            pair_in_last_iteration = True
    
    return pairs

def count_flush(card_list):
    """Counts the number of flushes in a card list.
    
    A flush is a sequence of 4 consecutive cards, all with different kinds.
    Each card can only belong to a single flush, so overlapping flushes are not counted.
    
    Parameters:
        card_list(list(str)): The list of cards to analyze.
        
    Returns:
        int: The number of flushes found.
        
    Examples:
        >>> count_flush(['hearts', 'spades', 'clubs', 'diamonds'])
        1
        >>> count_flush(['hearts', 'spades', 'clubs', 'diamonds', 'hearts', 'spades', 'clubs', 'diamonds'])
        2
        >>> count_flush(['hearts', 'hearts', 'clubs', 'diamonds'])
        0
        >>> count_flush(['hearts', 'spades', 'clubs'])
        0
        >>> count_flush([])
        0
        >>> count_flush(['hearts', 'spades', 'clubs', 'diamonds', 'spades'])
        1
        >>> count_flush(['hearts', 'spades', 'clubs', 'clubs', 'diamonds', 'hearts'])
        0
    """
    card_number = len(card_list)
    
    if card_number < 4:
        return 0
    
    # Counts the number of flushes found.
    flushes = 0
    
    # Keeps track of the cards being checked for a flush.
    # When this list holds 4 elements, a flush has been found.
    # When a flush is found, this list is reset.
    # When a repeated card is found, this list is reset.
    cards_to_check = []
    
    # We visit each card in the list.
    for i in range(0, card_number):
        # We obtain the card to check.
        card_to_check = card_list[i]
        
        # If the card is already in the cards_to_check list, there is no flush, we reset it.
        if card_to_check in cards_to_check:
            cards_to_check = []
            continue
        
        # If the card is not in the cards_to_check list, we add it.
        cards_to_check.append(card_to_check)
        
        # If we have 4 different cards, we found a flush, we increase the counter and reset the list.
        if len(cards_to_check) == 4:
            flushes += 1
            cards_to_check = []
    
    return flushes


def cut_cards(card_list, num_cuts):
    """Cuts the card_list into the specified number of parts and reorders them in reverse order.

    Parameters:
        card_list(list(str)): The cards to cut.
        num_cuts(int): The number of cuts to make.

    Returns:
        list(str): A new card list after being cut and reordered in reverse.

    Examples:
        >>> card_list = ['hearts', 'spades', 'clubs', 'diamonds', 'hearts2', 'spades2']
        >>> cut_cards(card_list, 2)
        ['diamonds', 'hearts2', 'spades2', 'hearts', 'spades', 'clubs']
        >>> cut_cards(card_list, 3)
        ['hearts2', 'spades2', 'clubs', 'diamonds', 'hearts', 'spades']
        >>> cut_cards(card_list, 1)
        ['hearts', 'spades', 'clubs', 'diamonds', 'hearts2', 'spades2']
        >>> cut_cards([], 2)
        []
        >>> cut_cards(['hearts'], 2)
        ['hearts']
    """
    card_number = len(card_list)
    
    # If there are no cards or only one cut, return a copy of the original list.
    if card_number == 0 or num_cuts <= 1:
        return card_list.copy()
    
    # Calculate the size of each cut
    cut_size = card_number // num_cuts
    
    # Create the cuts
    cuts = []
    
    # For each required cut we iterate once.
    for i in range(num_cuts):
        # Each cut starts at the number of the cut times the cut size
        start_index = i * cut_size
        if i == num_cuts - 1:  # Last cut takes all remaining cards
            end_index = card_number
        else:
            # Each cut ends at the start of the next cut
            end_index = (i + 1) * cut_size
            
        # Create the slice (the last index is not included)
        new_cut = card_list[start_index:end_index]
        
        # Add the cut to the list of cuts
        cuts.append(new_cut)
        
    # Reorder the cuts in reverse order
    new_card_list = []
    for cut in cuts:
        new_card_list = cut + new_card_list
    
    return new_card_list

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)