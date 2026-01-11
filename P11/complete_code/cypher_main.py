import cypher_logic
import cypher_user_io

OPTION_CYPHER_TEXT = "a"
OPTION_DECYPHER_TEXT = "b"
OPTION_FIND_CYPHERED_WORD = "c"
OPTION_CENSOR_TEXT = "d"
OPTION_EXIT = "z"

OPTIONS = (OPTION_CYPHER_TEXT, OPTION_DECYPHER_TEXT, OPTION_FIND_CYPHERED_WORD, OPTION_CENSOR_TEXT, OPTION_EXIT)

def show_menu():
    """Displays the menu options."""
    print('-' * 30)
    print("Menu Options:")
    print(f"{OPTION_CYPHER_TEXT}. Cypher text")
    print(f"{OPTION_DECYPHER_TEXT}. Decypher text")
    print(f"{OPTION_FIND_CYPHERED_WORD}. Find cyphered word")
    print(f"{OPTION_CENSOR_TEXT}. Censor text")
    print(f"{OPTION_EXIT}. Exit")
    print('-' * 30)

def ask_option():
    """Asks the user for a menu option."""
    option = ""
    while option not in OPTIONS:
        option = input("Select an option: ")
        if option not in OPTIONS:
            print("Invalid option. Please try again.")
        
    return option

def run_cypher_text():
    """Handles the cypher text functionality."""    
    text = input("Enter text to cypher: ")
    separator = cypher_user_io.ask_single_character("Enter a single character as separator: ")
    key = cypher_user_io.ask_key()
    
    cyphered_text = cypher_logic.cypher_text(text, separator, key)
    cypher_user_io.show_result("Cyphered text", cyphered_text)
    return text, cyphered_text, separator, key

def are_arguments_empty(cyphered_text, separator, key):
    """Checks if the cyphered text, separator, and key are valid."""

    return cyphered_text == "" or separator == "" or key == 0

def run_decypher_text(cyphered_text, separator, key):
    """Handles the decypher text functionality."""
    if are_arguments_empty(cyphered_text, separator, key):
        print("First you must cypher some text.")
        return

    decyphered = cypher_logic.decypher_text(cyphered_text, separator, key)
    cypher_user_io.show_result("Cyphered text", cyphered_text)
    cypher_user_io.show_result("Decyphered text", decyphered)   

def run_find_cyphered_word(cyphered_text, separator, key):
    """Handles finding a cyphered word."""
    if are_arguments_empty(cyphered_text, separator, key):
        print("First you must cypher some text.")
        return
    
    word = cypher_user_io.ask_single_word("Enter the word to find: ")
    
    result = cypher_logic.find_cyphered_word(word, cyphered_text, separator, key)
    count = cypher_logic.count_cyphered_word_occurrences(cyphered_text, separator, key, word)
    if result == cypher_logic.WORD_NOT_FOUND:
        print("Word not found")
    else:
        cypher_user_io.show_result("Cyphered text", cyphered_text)
        cypher_user_io.show_result("Cyphered word", result)
        cypher_user_io.show_result("Occurrences", count)
        
        
def run_count_occurrences(cyphered_text, separator, key):
    """Handles counting word occurrences in cyphered text."""
    if are_arguments_empty(cyphered_text, separator, key):
        print("First you must cypher some text.")
        return
    
    word = cypher_user_io.ask_single_word("Enter the word to count occurrences: ")
    
    count = cypher_logic.count_cyphered_word_occurrences(cyphered_text, separator, key, word)
    cypher_user_io.show_result("Cyphered word", word)
    cypher_user_io.show_result("Cyphered text", cyphered_text)
    cypher_user_io.show_result("Occurrences", count)

def run_censor_text(text):
    """Handles censoring text."""
    if text == "":
        print("No text available. Please cypher text first.")
        return
    
    word = cypher_user_io.ask_single_word("Enter the word to censor: ")
    symbol = cypher_user_io.ask_single_character("Enter a single character as replacement symbol: ")
    
    censored = cypher_logic.censor_text(text, word, symbol)

    cypher_user_io.show_result("Original text", text)
    cypher_user_io.show_result("Censored text", censored)

def handle_option(option, text, cyphered_text, separator, key):
    """Handles the selected menu option."""
    if option == OPTION_CYPHER_TEXT:
        text, cyphered_text, separator, key = run_cypher_text()
    elif option == OPTION_DECYPHER_TEXT:
        run_decypher_text(cyphered_text, separator, key)
    elif option == OPTION_FIND_CYPHERED_WORD:
        run_find_cyphered_word(cyphered_text, separator, key)
    elif option == OPTION_CENSOR_TEXT:
        run_censor_text(text)
    elif option == OPTION_EXIT:
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid option selected.")
        
    return text, cyphered_text, separator, key

def main():
    """Main program loop."""
    option = ""
    text = ""
    cyphered_text = ""
    separator = ""
    key = 0
    while option != OPTION_EXIT:
        show_menu()
        option  = ask_option()
        text, cyphered_text, separator, key = handle_option(option, text, cyphered_text, separator, key)

if __name__ == "__main__":
    main()