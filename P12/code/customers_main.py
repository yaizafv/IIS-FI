import customers_file_io as file_io
import customers_user_io as user_io
import customers_logic as logic
# Menu option constants
OPTION_NONE = ""
OPTION_SHOW_CUSTOMERS = "a"
OPTION_ADD_CUSTOMER = "b"
OPTION_UPDATE_CUSTOMER_SUBSCRIPTION = "c"
OPTION_FILTER_ACTIVE_SUBSCRIBERS = "d"
OPTION_SHOW_TOTAL_REVENUE = "e"
OPTION_LIST_SORTED_CUSTOMERS = "f"
OPTION_GENERATE_REPORTS = "g"
OPTION_EXIT = "q"

# File path for storing customer data
CUSTOMERS_FILE = "customers.csv"
CUSTOMERS_TXT = "customers.txt"
# Field separator used in customer CSV file
SEPARATOR = ";"

def run_show_customers():
    """Reads the customers file and prints its contents in the console."""
    customers = file_io.load_clients(CUSTOMERS_FILE, SEPARATOR)
    user_io.show_customers(customers)


def run_add_customer():
    """
    Requests data for a single customer and saves it at the end of the customers file.
    This function interacts with the user to get customer information,
    then attempts to save it using the customers_file_io module.
    """
    customer = user_io.ask_customer_data()
    file_io.save_new_customer(CUSTOMERS_FILE, SEPARATOR, customer)


def run_update_subscription():
    """Requests the user the dni and subscription update of a client, and updates the file."""
    customers = file_io.load_clients(CUSTOMERS_FILE, SEPARATOR)
    dni, suscription = user_io.ask_subscription_update_data()
    updated_customers = logic.update_suscription(customers, dni, suscription)



def run_generate_reports():
    """Reads the clients file and generates a report for each customer in it."""
    customers = file_io.load_clients(CUSTOMERS_FILE, SEPARATOR)
    for client in customers:
        file_io.save_report(CUSTOMERS_TXT, client)


def run_filter_customers():
    """Reads the customers file and shows only those which are currently subscribed."""
    customers = file_io.load_clients(CUSTOMERS_FILE, SEPARATOR)
    filter_list = logic.filter_subscribed_clients(customers)
    print(filter_list)


def run_show_total_revenue():
    """Reads the clients file and shows the total revenue."""
    customers = file_io.load_clients(CUSTOMERS_FILE, SEPARATOR)
    total_costs = logic.calculate_total_revenue(customers)
    print(total_costs)


def run_show_customers_sorted():
    """Reads the clients file and shows the list sorted by name."""
    customers = file_io.load_clients(CUSTOMERS_FILE, SEPARATOR)
    ordered_list = logic.sort_customers_by_name(customers)
    print(ordered_list)


def show_menu():
    """Displays the main menu and returns the selected option."""
    print("\n--- Management Menu ---")
    print(f"{OPTION_SHOW_CUSTOMERS} - Show all customers")
    print(f"{OPTION_ADD_CUSTOMER} - Add new customer")
    print(f"{OPTION_UPDATE_CUSTOMER_SUBSCRIPTION} - Update customer subscription")
    print(f"{OPTION_GENERATE_REPORTS} - Generate customer reports")
    print(f"{OPTION_FILTER_ACTIVE_SUBSCRIBERS} - Filter subscribed customers")
    print(f"{OPTION_SHOW_TOTAL_REVENUE} - Show total revenue")
    print(f"{OPTION_LIST_SORTED_CUSTOMERS} - Show customers sorted by name")
    print(f"{OPTION_EXIT} - Exit")
    return input("Choose an option: ")


def handle_option(selected_option):
    """Executes the corresponding action based on the selected option."""

    if selected_option == OPTION_SHOW_CUSTOMERS:
        run_show_customers()
    elif selected_option == OPTION_ADD_CUSTOMER:
        run_add_customer()
    elif selected_option == OPTION_UPDATE_CUSTOMER_SUBSCRIPTION:
        run_update_subscription()
    elif selected_option == OPTION_GENERATE_REPORTS:
        run_generate_reports()
    elif selected_option == OPTION_FILTER_ACTIVE_SUBSCRIBERS:
        run_filter_customers()
    elif selected_option == OPTION_SHOW_TOTAL_REVENUE:
        run_show_total_revenue()
    elif selected_option == OPTION_LIST_SORTED_CUSTOMERS:
        run_show_customers_sorted()

    elif selected_option == OPTION_EXIT:
        print("Exiting program...")
    else:
        print("Invalid option.")



def main():
    """Main loop of the application."""
    selected_option = OPTION_NONE
    while selected_option != OPTION_EXIT:
        selected_option = show_menu()
        handle_option(selected_option)


if __name__ == "__main__":
    main()
