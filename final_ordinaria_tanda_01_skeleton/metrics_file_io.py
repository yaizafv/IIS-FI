def load_contents_dict(filename_list):
    """Receives a list of text file paths and returns a dictionary with
    their names as keys and their text contents as values.

    Args:
        filename_list (list(str)): A list of paths to text files to be read.

    Raises:
        ValueError: If the provided list is empty.

    Returns:
        dict(str, str): The contents of the files as a dictionary.
            - The keys are the file names.
            - The values are the full text contents of each file.
    """
    if len(filename_list) == 0:
        raise ValueError("The list of file names cannot be empty")

    files_contents = {}
    for filename in filename_list:
        try:
            with open(filename, "r") as file:
                file_text = file.read()

            files_contents[filename] = file_text
        except FileNotFoundError:
            print(f"File filename {filename} not found, skipping it.")

    return files_contents


def load_file_list(filename):
    """Load a csv semi-colon separated file list and return file paths.

    The expected file format is one entry per line with three
    semi-colon separated fields: 'title;path;description'. Only the
    'path' field is returned.

    Args:
        filename (str): Path to the file that lists other files.

    Raises:
        ValueError: If the filename is an empty string.
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a line does not contain exactly three fields when
            split by ';'.

    Returns:
        list(str): A list with the 'path' values extracted from each line.
    """
    if filename == '':
        raise ValueError("filename cannot be empty")
    
    list_result = []
    
    try:
        with open(filename, "r") as f:
            line = f.readline()
            while line != "":
                line_strip = line.strip()
                line_split = line_strip.split(";")
                if len(line_split) != 3:
                    raise ValueError("len of line must be 3")
                path = line_split[1]
                list_result.append(path)
                line = f.readline()
    except FileNotFoundError as fnf:
        print("error buscando el fichero: " + fnf)
        
    return list_result


def save_metrics(filename, metrics_list):
    """Saves a list of metrics dictionaries to 'filename'.

    The output format is one entry per line with fields separated by semi-colons: title;text_length;alphanumerics_count

    Args:
        filename (str): Path to the output file to write.
        metrics_list (list(dict)): A List containing metrics dictionaries.
            Each metrics dictionary in the list has the keys:
            - (str: str)'name': The name for the provided text.
            - (str: int)'text_length': Total number of characters in the analyzed text.
            - (str: int)'alphanumerics_count': Total number of alphanumeric characters in the analyzed text.

    Raises:
        ValueError: If the file name is empty.
        ValueError: If the metrics list is empty.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        for metrics in metrics_list:
            line = (
                f"{metrics[KEY_NAME]};"
                f"{metrics[KEY_TEXT_LENGTH]};"
                f"{metrics[KEY_ALPHANUMERICS_COUNT]};"
            )
            f.write(line)
