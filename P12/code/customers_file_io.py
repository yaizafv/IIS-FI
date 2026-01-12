def _generate_report_text(
    name, dni, active_subscription, subscription_time, total_expenses
):
    """
    Generates a report text for a customer.

    Args:
        name (str): The name of the customer.
        dni (str): The DNI of the customer.
        active_subscription (bool): Whether the subscription is active.
        subscription_time (tuple(int, int)): The subscription time in years (int) and months (int).
        total_expenses (float): The total expenses of the customer.

    Returns:
        str: The formatted report text.
    """
    # Unpack the subscription time tuple
    years, months = subscription_time

    # Convert boolean to user-friendly string
    if active_subscription:
        active_subscription_str = "Yes"
    else:
        active_subscription_str = "No"

    # Build the report string with proper formatting and indentation
    report = f"Report for {name}, {dni}\n"
    report += f"\t-Time subscribed: {years} years, {months} months\n"
    report += f"\t-Active subscription : {active_subscription_str}\n"
    report += f"\t-Total expenses: {total_expenses} €\n"

    return report

def save_report(filename, client):
    name, dni, active_subscription, total_months, total_expenses = client
    years = total_months // 12
    months = total_months % 12
    subscription_time = (years, months)
    report = _generate_report_text(name, dni, active_subscription, subscription_time, total_expenses)
    write_file(filename, "a", report)


def load_clients(filename, separator):
    clients = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, dni, sub_type, months, active = line.split(separator)
            clients.append((
                name,
                dni,
                float(sub_type),
                int(months),
                active in ("Y")
            ))

    return clients

def save_new_customer(filename, separator, client):
    client_string = generate_client_string(client, separator)
    write_file(filename, "a", client_string)

def generate_client_string(client, separator):
    name, dni, sub_type, months, active = client
    active_str = "Y" if active else "N"
    fields = [
        name,
        dni,
        str(sub_type),
        str(months),
        active_str
    ]
    return separator.join(fields) + "\n"

def update_customers(filename, separator, clients):
    with open(filename, "w", encoding="utf-8") as f:
        for client in clients:
            f.write(generate_client_string(client, separator))

def write_file(filename, type_to_open , content):       ## only accepts 'w' or 'a'
    with open(filename, type_to_open, encoding="utf-8") as f:
        f.write(content)



