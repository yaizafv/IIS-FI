KEY_Name = "name"
KEY_TEXT_LENGTH = "text_length"
KEY_ALPHANUMERICS_COUNT = "alphanumerics_count"


def create_character_counter_dict(text):
    char_counter = {}
    for char in text:
        if char not in char_counter:
            char_counter[char] = 0
        char_counter[char] += 1
    return char_counter


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
    ######################################################################################################
    # Obtain the number of alphanumeric characters in the text so that it can be added to the dictionary #
    ######################################################################################################

    metrics = {
        KEY_Name: title,
        KEY_TEXT_LENGTH: len(text),
        KEY_ALPHANUMERICS_COUNT: "?????",  # CHANGE THIS LINE TO ASSIGN THE NUMBER OF ALPHANUMERIC CHARACTERS
    }

    return metrics
