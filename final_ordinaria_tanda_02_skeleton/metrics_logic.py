KEY_NAME = "name"
KEY_TEXT_LENGTH = "text_length"
KEY_MOST_REPEATED_CHARACTER_COUNT = "most_repeated_character_count"
KEY_MOST_REPEATED_CHARACTER = "most_repeated_character"


def create_character_indexes_dict(text):
    char_indexes = {}
    index = 0
    for char in text:
        if char not in char_indexes:
            char_indexes[char] = []
        char_indexes[char].append(index)
        index += 1
    return char_indexes


def get_most_repeated_character_and_count(character_indexes_dict):
    if not character_indexes_dict:
        return (None, 0)
    
    most_repeated_char = None
    most_repeated_count = 0
    
    for char in character_indexes_dict:
        count = len(character_indexes_dict[char])
        if count > most_repeated_count:
            most_repeated_count = count
            most_repeated_char = char
    
    return (most_repeated_char, most_repeated_count)


def create_metrics_dict_from_text(title, text):
    ##############################################################################################
    # Obtain the most repeated character and its count so that it can be added to the dictionary #
    ##############################################################################################
    metrics = {
        KEY_NAME: title,
        KEY_TEXT_LENGTH: len(text),
        KEY_MOST_REPEATED_CHARACTER_COUNT: "????????",  # CHANGE THIS LINE TO ASSIGN THE COUNT OF THE MOST REPEATED CHARACTER
        KEY_MOST_REPEATED_CHARACTER: "????????",  # CHANGE THIS LINE TO ASSIGN THE MOST REPEATED CHARACTER
    }

    return metrics


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
