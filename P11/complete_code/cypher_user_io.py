import cypher_logic


def ask_single_word(message):
    """Asks the user for a word.
    Args:
        message (str): The message to show to the user.
    Returns:
        str: The word entered by the user.
    """
    word = ""
    while ' ' in word or word == "":
        word = input(message)
        if ' ' in word or word == "":
            print("Invalid input. Please enter a single word without spaces.")

    return word

def ask_single_character(message):
    """Asks the user for a single character.
    Args:
        message (str): The message to show to the user.
    Returns:
        str: The single character entered by the user.
    """
    character = ""
    while len(character) != 1:
        character = input(message)
        if len(character) != 1:
            print("Invalid input. Please enter exactly one character.")
    return character

def ask_key():
    """Asks the user for a key.
    Returns:
        int: The key entered by the user.
    """
    key = 0
    while key < 1 or key > cypher_logic.MAX_SHIFT:
        try:
            key_str = input(f"Enter key (1-{cypher_logic.MAX_SHIFT}): ")
            key = int(key_str)
            if key < 1 or key > cypher_logic.MAX_SHIFT:
                print(f"Key must be between 1 and {cypher_logic.MAX_SHIFT}. Please try again.")
        except ValueError:
            print("Invalid number.")

    return key

def show_result(title, result):
    """Prints the result with a title.
    Args:
        title (str): The title of the result.
        result (str): The result to show.
    """
    print(f"{title}: {result}")



