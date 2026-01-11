MAX_SHIFT = 27
WORD_NOT_FOUND = -1

def validate_key(key):
    """ Validates that the key is within the acceptable range.
    Args:
        key (int): The integer value to validate.
    Raises:
        ValueError: If the key is not between -LETTER_NUMBER and LETTER_NUMBER.
    Examples:
        >>> validate_key(1)
        >>> validate_key(27)
        >>> validate_key(0)
        Traceback (most recent call last):
        ...
        ValueError: Key cannot be lower than 1.
        >>> validate_key(28)
        Traceback (most recent call last):
        ...
        ValueError: Key must be lower than 27.

    """
    if key < 1:
        raise ValueError('Key cannot be lower than 1.')
    if key > MAX_SHIFT:
        raise ValueError(f'Key must be lower than {MAX_SHIFT}.')
    
def shift_word(word, key):
    """ Shifts a word by shifting each character's ASCII value by the given key.
    Args:
        word (str): The word to be shifted.
        key (int): The integer value to shift each character's ASCII value.
    Raises:
        ValueError: If the key is not between -LETTER_NUMBER and LETTER_NUMBER.
    Returns:
        str: The shifted word.
    Examples:
        >>> shift_word("abc", 1)
        'bcd'
        >>> shift_word('bcd', -1)
        'abc'
        >>> shift_word('abc', -35)
        '>?@'
        >>> shift_word('xyz', 0)
        'xyz'
    """
    result = ""
    for character in word:
        ascii = ord(character)
        shifted_ascii = ascii + key
        shifted_character = chr(shifted_ascii)
        result += shifted_character

    return result

def shift_text(text, split_separator, join_separator, key):
    """ Shifts a text by splitting it into words using the given split separator,
        shifting each word, and joining them back with the given join separator.
    Args:
        text (str): The text to be shifted.
        split_separator (str): The separator used to split the words.
        join_separator (str): The separator used to join the shifted words.
        key (int): The integer value to shift each character's ASCII value.
    Returns:
        str: The shifted text.
    Examples:
        >>> shift_text("abc def ghi", " ", ":", 1)
        'bcd:efg:hij'
        >>> shift_text('bcd:efg:hij', ":", " ", -1)
        'abc def ghi'
        >>> shift_text("Hello", " ", " ", 0)
        'Hello'
    """
    shifter_words = text.split(split_separator)
    shifted_words = []
    for word in shifter_words:
        shifted_word = shift_word(word, key)
        shifted_words.append(shifted_word)
    shifted_text = join_separator.join(shifted_words)
    return shifted_text

def cypher_text(text, separator, key):
    """ Cyphers a text by splitting it into words using the given separator,
        cyphering each word, and joining them back with the same separator.
    Args:
        text (str): The text to be cyphered.
        separator (str): The separator used to split and join the words.
        key (int): The integer value to shift each character's ASCII value.
    Returns:
        str: The cyphered text.
    Examples:
        >>> cypher_text("Hello everybody there", " ", 1)
        'Ifmmp#fwfszcpez#uifsf'
        >>> cypher_text("abc:def:ghi", ":", 2)
        'cde#fgh#ijk'
        >>> cypher_text("Hello", " ", 0)
        Traceback (most recent call last):
        ...
        ValueError: Key cannot be lower than 1.
        >>> cypher_text("Hello", " ", 28)
        Traceback (most recent call last):
        ...
        ValueError: Key must be lower than 27.
    """
    validate_key(key)
    
    cyphered_text = shift_text(text, separator, '#', key)
    return cyphered_text

def decypher_text(cyphered_text, separator, key):
    """ Decyphers a text by splitting it into words using the given separator,
        decyphering each word, and joining them back with the same separator.
    Args:
        text (str): The text to be decyphered.
        separator (str): The separator used to split and join the words.
        key (int): The integer value to shift each character's ASCII value back.
    Returns:
        str: The decyphered text.
    Examples:
        >>> decypher_text("Ifmmp#fwfszcpez#uifsf", " ", 1)
        'Hello everybody there'
        >>> decypher_text("cde#fgh#ijk", ":", 2)
        'abc:def:ghi'
        >>> decypher_text("Hello", " ", 0)
        Traceback (most recent call last):
        ...
        ValueError: Key cannot be lower than 1.
        >>> decypher_text("Hello", " ", 28)
        Traceback (most recent call last):
        ...
        ValueError: Key must be lower than 27.
    """
    validate_key(key)

    decyphered_text = shift_text(cyphered_text, '#', separator, -key)
    return decyphered_text

def find_cyphered_word(word, cyphered_text, key):
    """ Finds the cyphered version of a given word within a cyphered text.
    Args:
        word (str): The original word to find.
        cyphered_text (str): The cyphered text to search within.
        key (int): The integer value used for cyphering.
        Returns:
        str: The cyphered version of the word if found, otherwise -1.
        Examples:
        >>> find_cyphered_word("Hello", "Ifmmp#fwfszcpez#uifsf", 1)
        'Ifmmp'
        >>> find_cyphered_word("abc", "cde#fgh#ijk", 2)
        'cde'
        >>> find_cyphered_word("xyz", "abc#def#ghi", 2)
        -1
    """
    validate_key(key)
    decyphered_text = decypher_text(cyphered_text, " ", key)
    word_index = decyphered_text.find(word)
    if word_index == -1:
        return WORD_NOT_FOUND           
    
    word_length = len(word)
    end_position = word_index + word_length
    cyphered_word = cyphered_text[word_index:end_position]
    
    return cyphered_word

def count_cyphered_word_occurrences(cyphered_text, key, censored_word):
    """ Counts the occurrences of a cyphered word in a cyphered text.
    Args:
        cyphered_text (str): The cyphered text to search within.
        key (int): The integer value used for cyphering.
        censored_word (str): The original word to count occurrences of.
    Returns:
        int: The number of occurrences of the cyphered word in the cyphered text.
    Examples:
        >>> count_cyphered_word_occurrences("Ifmmp#Xpsme#Ifmmp", 1, "Hello")
        2
        >>> count_cyphered_word_occurrences("cde#fgh#ijk#cde", 2, "abc")
        2
        >>> count_cyphered_word_occurrences("abc#def#ghi", 2, "xyz")
        0
    """
    cyphered_word = find_cyphered_word(censored_word, cyphered_text, key)
    if cyphered_word == -1:
        return 0

    occurrences = cyphered_text.count(cyphered_word)
    
    return occurrences

def censor_text(text, censored_word, censor_symbol):    
    """ Censors a given word in the text by replacing it with a censor symbol.
    Args:
        text (str): The original text.
        censored_word (str): The word to be censored.
        censor_symbol (str): The symbol to replace the censored word with.
    Returns:
        str: The censored text.
    Examples:
        >>> censor_text("Hello World", "World", "*")
        'Hello *****'
        >>> censor_text("abc def ghi", "def", "#")
        'abc ### ghi'
    """
    word_length = len(censored_word)
    word_substitute = censor_symbol * word_length
    censored_text = text.replace(censored_word, word_substitute)
    return censored_text



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)