def ask_positive_integer(message):
    """
    Prompts the user to enter a positive integer using the provided message.
    Validates the input and keeps asking until a valid positive integer is entered.

    Args:
        message (str): The message to display when asking for input.

    Returns:
        int: A positive integer (>= 0).
    """
    # Initialize with invalid value to ensure loop runs at least once
    positive_integer = -1

    # Keep asking until user enters a valid positive integer
    while positive_integer < 0:
        try:
            # Attempt to convert user input to integer
            positive_integer = int(input(message))
            # Check if the number is negative
            if positive_integer < 0:
                print("The value must be positive, try again.")
        except ValueError:
            # Handle case where user enters non-numeric input
            print("You introduced an invalid number, try again.")

    return positive_integer


def ask_yes_no_question(message):
    """
    Prompts the user with a yes/no question and validates the response.
    Accepts 'Y' or 'N' (case insensitive) and keeps asking until valid input is provided.

    Args:
        message (str): The question message to display to the user.

    Returns:
        bool: True if the user answered 'Y', False if the user answered 'N'.
    """


def ask_customer_data():
    """
    Prompts the user to enter customer data via standard input.

    Returns:
        tuple: A tuple containing (name, dni, subscription_plan_amount, months_subscribed, is_active_subscription).
    """
    # Get basic customer information
    name = input("Customer name: ")
    dni = ask_dni()
    subscriber_plan_amount = ask_subscriber_plan_amount()
    months_subscribed = ask_positive_integer("Enter the number of months subscribed: ")
    is_active_subscription = ask_is_subscription_active()

    # Return all customer data as a tuple
    return (
        name,
        dni,
        subscriber_plan_amount,
        months_subscribed,
        is_active_subscription,
    )


def ask_dni():
    """
    Prompts the user to enter a valid Spanish DNI (8 digits + 1 letter).
    Validates the format and keeps asking until a valid DNI is entered.

    Returns:
        str: A valid DNI string with 8 digits followed by one letter.
    """
    # Initialize with invalid value to ensure loop runs
    dni = "0"

    # Keep asking until DNI meets all validation criteria
    while (len(dni) != 9) or (not dni[-1].isalpha()) or (not dni[0:8].isdigit()):
        dni = input("Customer DNI (8 digits and one letter): ")

        # Print a message if length validation is incorrect (must be exactly 9 characters)
        if len(dni) != 9:
            print(
                f"Error: The introduced DNI should have 9 characters, you introduced {len(dni)}, try again."
            )
        # Print a message if last character is not a letter
        elif not dni[-1].isalpha():
            print(
                f"Error: The last character must be a letter, you introduced {dni}, try again."
            )
        # Print a message if first 8 characters are not digits
        elif not dni[0:8].isdigit():
            print(
                f"Error: The first 8 characters must be digits, you introduced {dni}, try again."
            )

    return dni


def ask_subscriber_plan_amount():
    """
    Prompts the user to enter a valid subscription plan amount.
    Only accepts 9.90 or 14.90 as valid values.

    Returns:
        float: The subscription plan amount (either 9.90 or 14.90).
    """
    # Initialize with invalid value to ensure loop runs
    subscriber_plan_amount = 0

    # Keep asking until user enters one of the valid subscription amounts
    while subscriber_plan_amount != 9.90 and subscriber_plan_amount != 14.90:
        try:
            # Attempt to convert user input to float
            subscriber_plan_amount = float(
                input("Enter the price of the subscriber's plan (9.90 or 14.90): ")
            )

            # Print a message if the amount is one of the valid options
            if subscriber_plan_amount != 9.90 and subscriber_plan_amount != 14.90:
                print(
                    f"The introduced amount must be either 9.90 or 14.90, you introduced {subscriber_plan_amount}, try again."
                )
        except ValueError:
            # Handle case where user enters non-numeric input
            print("You introduced an invalid number, try again.")

    return subscriber_plan_amount


def ask_is_subscription_active():
    """
    Prompts the user to indicate if a client's subscription is currently active.

    Returns:
        bool: True if the subscription is active (Y), False otherwise (N).
    """
    # Initialize with empty string to ensure loop runs
    yes_no_str = ""

    # Keep asking until user enters 'Y' or 'N'
    while yes_no_str != "Y" and yes_no_str != "N":
        # Get user input
        yes_no_str = input("Is the client currently subscribed (Y/N): ")

        # Convert to uppercase to handle case insensitive input (y, n, Y, N)
        yes_no_str = yes_no_str.upper()

        # Check if input is still invalid after conversion
        if yes_no_str != "Y" and yes_no_str != "N":
            print("Error: You must write either 'Y' or 'N', try again: ")

    # Convert string response to boolean: 'Y' becomes True, 'N' becomes False
    is_subscription_active = yes_no_str == "Y"

    return is_subscription_active


def ask_subscription_update_data():
    """Asks the user the necessary data to update the subscription status of a client.
    First requests the dni, then if it'ts subscription is active (Y/N).

    Returns:
        tuple(str, bool): Returns a tuple with the dni(str) and the current subscription status (bool).
    """
    print("You are going to update the subscription status of a client.")
    dni = ask_dni()
    subscription_active = ask_is_subscription_active()

    return dni, subscription_active


def show_customers(customers):
    """
    Displays the list of customers on the screen.

    Args:
        customers (list): List of customers to display.
    """
    # If the customers list is empty, inform the user and exit the function
    if not customers:
        print("No customers registered.")
        return

    # Print the header for the customer list
    print("\nCustomer List")

    # Note:
    # The formatting string `:<20` in f-strings (e.g., f"{name:<20}") means:
    #   - Align the value to the left (`<`)
    #   - Fill the field to a width of 20 characters (`20`)
    # This ensures that all columns are aligned and have the same width in the output.
    print(
        f"{'Name':<20} {'DNI':<20} {'Plan':<20} {'Months subscribed':<20} {'Active subscription':<20}"
    )
    # Print a separator line for better readability
    print("-" * 100)

    # Iterate through each customer and print their details in a formatted way
    for customer in customers:
        name, dni, subscription_plan, months_subscribed, active_subscription = customer

        # Convert the boolean active_subscription to 'Y' or 'N' for display
        if active_subscription:
            active_subscription_str = "Y"
        else:
            active_subscription_str = "N"

        # Print the customer information in aligned columns
        print(
            f"{name:<20} {dni:<20} {subscription_plan:<20} {months_subscribed:<20} {active_subscription_str:<20}"
        )
