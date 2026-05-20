def load_contents_dict(filename_list):
    """Read and return the full contents of ``filename`` as a string.

    Args:
        filename (str): Path to a text file to be read.

    Returns:
        str: The contents of the file.

    Notes:
        This uses the system default text encoding. Callers that require
        a specific encoding should open the file themselves.
    """
    if len(filename_list) == 0:
        raise ValueError('The list of file names cannot be empty')
    
    files_contents = {}
    for filename in filename_list:
        try:
            with open(filename, 'r') as file:
                file_text = file.read()
                
            files_contents[filename] = file_text
        except FileNotFoundError as exc:
            print(f'File filename {filename} not found, skipping it.')

    return files_contents


def load_file_list(filename):
    """Load a semi-colon separated file list and return file paths.

    The expected file format is one entry per line with three
    semi-colon separated fields: title;path;description. Only the
    path field is returned.

    Args:
        filename (str): Path to the file that lists other files.

    Returns:
        list[str]: A list with the path values extracted from each line.

    Raises:
        ValueError: If a line does not contain exactly three fields when
            split by ';'.
    """
    pass


def save_metrics(filename, metrics_list):
    """Saves a list of metrics dictionaries to 'filename'.

    The output format is one entry per line with fields separated by semi-colons: 
    title;text_length;most_repeated_character_count;most_repeated_character

    Args:
        filename (str): Path to the output file to write.
        metrics_list (list(dict)): A List containing metrics dictionaries.
            Each metrics dictionary in the list has the keys:
            - 'title' (str): The provided title (str).
            - 'text_length' (str): Total number of characters in 'text' (int).
            - 'most_repeated_character_count' (str): Total number of occurrences of the most repeated character in 'text' (int).
            - 'most_repeated_character' (str): The most repeated character in 'text' (str).
            The constants for these titles are available as KEY_TITLE, KEY_TEXT_LENGTH, KEY_MOST_REPEATED_CHARACTER_COUNT, and KEY_MOST_REPEATED_CHARACTER
            in the metrics_logic module.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        for metrics in metrics_list:
            line = (
                f"{metrics[KEY_NAME]};"
                f"{metrics[KEY_TEXT_LENGTH]};"
                f"{metrics[KEY_MOST_REPEATED_CHARACTER_COUNT]};"
                f"{metrics[KEY_MOST_REPEATED_CHARACTER]}\n"
            )
            f.write(line)