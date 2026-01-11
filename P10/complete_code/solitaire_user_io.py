# Constant for the width of each column when printing. Can be adjusted as needed.
COLUMN_WIDTH = 20

def greatest_column_size(columns):
    """ Returns the size of the greatest column in the list of columns.
    This is used to determine how many rows need to be printed when displaying the columns.
    
    Args:
        columns (list of list of str): The columns of cards.
    Returns:
        int: The size of the greatest column.
    """
    greatest_size = 0
    for column in columns:
        if len(column) > greatest_size:
            greatest_size = len(column)

    return greatest_size

def get_columns_element_string(columns, row_index, column_index):
    """Returns the string representation of the element in the given row and column.
    it follows the format: [column_index][row_index]element
    If there is no element in that position, returns an empty string.
    
    Args:
        columns (list of list of str): The columns of cards.
        row_index (int): The row index of the element.
        column_index (int): The column index of the element.
        
    Returns:
        str: The string representation of the element in format [column_index][row_index]element, or an empty string if there is no element.
    """
    # We get the column.
    column = columns[column_index]
    
    # If the row index is greater than the length of the column, there is no element.
    if row_index < len(column): # If there is an element in that position we get that element info.
        column_content = f"[{column_index}][{row_index}]{column[row_index]}"
    else: # If there is no element in that position we return an empty string.
        column_content = ""

    return column_content

def show_columns(columns):
    """Displays the columns of cards in a formatted table layout.
    Each card is shown with its position [column_index][row_index] and value.
    All columns are aligned using a fixed width for readability.
    
    Args:
        columns (list of list of str): The columns of cards to display.
    """
    # We get the size of the greatest column.
    # We need this to know how many rows we have to print.
    # We can't just get the size of the first column, because other columns may be greater.
    greatest_size = greatest_column_size(columns)

    # We print each row.
    for row_index in range(greatest_size):
        # We start with an empty string for the row.
        row_string = ""

        # We add each column's content to the row.
        for column_index in range(len(columns)):
            # If the column has an element it will add its string.
            # If the column doesn't have an element in this row, it will add an empty string.
            column_content = get_columns_element_string(columns, row_index, column_index)

            # We add the column content to the row string.
            # The ljust fills with empty spaces the string to make sure that each column takes the same width regardless of its content
            # This makes the columns properly aligned even if there are empty elements.
            row_string += column_content.ljust(COLUMN_WIDTH)

        # We print the row. after visiting all columns.
        print(row_string)

def ask_indexes(message):
    column = -1
    row = -1
    print(message)
    while row < 0 or column < 0:
        try:
            column = int(input("Introduce the column index: "))
            row = int(input("Introduce the row index: "))
        except ValueError:
            print("Invalid integer, try again.")

    return column, row


def ask_indexes(message):
    """Asks the user to input column and row indexes.
    The function will keep asking until valid positive integers are provided.
    
    Args:
        message (str): The message to display to the user before asking for input.
        
    Returns:
        tuple: A tuple containing (column, row) as integers.
    """
    # Initialize column and row with invalid values to enter the loop
    column = -1
    row = -1
    
    # Display the message to the user
    print(message)
    
    # Keep asking until both values are valid (non-negative)
    while row < 0 or column < 0:
        try:
            # Ask for column and row indexes
            column = int(input("Introduce the column index: "))
            row = int(input("Introduce the row index: "))
        except ValueError:
            # If the user enters a non-integer value, show error and try again
            print("Invalid integer, try again.")

    return column, row


def ask_move(columns):
    """Asks the user to input origin and destination positions for a move.
    The function validates that both positions exist in the columns structure.
    It will keep asking until valid positions are provided.
    
    Args:
        columns (list of list of str): The columns of cards to validate positions against.
        
    Returns:
        tuple: A tuple containing ((origin_row, origin_column), (destination_row, destination_column)).
    """
    # Initialize values to -1 to indicate they haven't been set yet
    origin_value = -1
    destination_value = -1
    
    # Keep asking for origin until a valid position is provided
    while origin_value == -1:
        try:
            # Ask for origin indexes
            origin_position = ask_indexes("Introduce the origin column and row.")
            origin_row, origin_column = origin_position
            
            # Try to access the position to verify it exists
            # This will raise an IndexError if out of bounds
            origin_value = columns[origin_column][origin_row]
 
        except IndexError:
            # If the position doesn't exist, show error and ask again
            print("The provided indexes for the origin are out of bounds, try again.")
    
    # Keep asking for destination until a valid position is provided
    while destination_value == -1:
        try:
            # Ask for destination indexes
            destination_position = ask_indexes("Introduce the destination column and row.")
            destination_row, destination_column = destination_position
            
            # Try to access the position to verify it exists
            # This will raise an IndexError if out of bounds
            destination_value = columns[destination_column][destination_row]

        except IndexError:
            # If the position doesn't exist, show error and ask again
            print("The provided indexes for the destination are out of bounds, try again.")
       
    return origin_position, destination_position