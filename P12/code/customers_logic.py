def update_suscription(clients, dni_to_update, activate):
    """
    Updates the subscription status of a client identified by DNI.

    Args:
        clients (list): List of client tuples.
        dni_to_update (str): DNI of the client to update.
        activate (bool): True to activate, False to deactivate.

    Returns:
        list: New list of clients with updated subscription.

    Example:
    >>> test_customers = [
    ...     ("Juan Pérez", "12345678A", 10.0, 12, True),
    ...     ("María López", "23456789B", 15.0, 24, False)
    ... ]
    >>> update_suscription(test_customers, "23456789B", True)
    [('Juan Pérez', '12345678A', 10.0, 12, True), ('María López', '23456789B', 15.0, 24, True)]
    >>> update_suscription(test_customers, "12345678A", False)
    [('Juan Pérez', '12345678A', 10.0, 12, False), ('María López', '23456789B', 15.0, 24, False)]
    """
    updated_clients = []
    for client in clients:
        name, dni, sub_type, months, active = client
        if dni == dni_to_update:
            updated_clients.append((name, dni_to_update, sub_type, months, activate))
        else:
            updated_clients.append(client)
    return updated_clients

def filter_subscribed_clients(clients):
    filter_list = []
    for client in clients:
        name, dni, sub_type, months, active = client
        if active:
            filter_list.append(client)
    return filter_list

def calculate_total_revenue(clients):
    total_costs = 0
    for client in clients:
        name, dni, sub_type, months, active = client
        total_costs += sub_type
    return total_costs

def sort_customers_by_name(clients):
    """
    Returns a new list of clients sorted alphabetically by name
    without using sorted() or enumerate.

    Args:
        clients (list): List of client tuples.

    Returns:
        list: New list sorted by client name.
    """
    # return sorted(clients)
    sorted_clients = []  # lista nueva vacía
    for client in clients:  # recorrer lista original
        inserted = False
        # recorrer la lista ordenada usando índices
        for index in range(len(sorted_clients)):
            sorted_client = sorted_clients[index]
            if client[0] < sorted_client[0]:  # comparar nombres
                sorted_clients.insert(index, client)  # insertar en esa posición
                inserted = True
                break  # salir del bucle interno
        if not inserted:  # si no se insertó, añadir al final
            sorted_clients.append(client)

    return sorted_clients

if __name__ == "__main__":
    # repeat the previous code
    import doctest
    # Define test data only when running doctests
    # This data represents: (name, dni, monthly_subscription, months_subscribed, is_active)
    test_customers = [
        ("Juan Pérez", "12345678A", 10.0, 12, True),
        ("María López", "23456789B", 15.0, 24, False),
        ("Carlos García", "34567890C", 12.5, 6, True),
        ("Ana Fernández", "45678901D", 20.0, 18, True),
        ("Luis Martínez", "56789012E", 8.0, 3, False),
    ]   
    # Inject the test data into doctest namespace without creating global variables
    doctest.testmod(extraglobs={"customers": test_customers}, verbose=True)