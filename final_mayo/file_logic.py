def parse_sessions(lista):
    """
    Examples:
    >>> parse_sessions(["languaje;67;5", "science;87;7"])
    [('languaje', 67, 5), ('science', 87, 7)]

    >>> parse_sessions([])
    Traceback (most recent call last):
    ...
    ValueError: la lista no puede estar vacia
    
    >>> parse_sessions(["test;5"])
    Traceback (most recent call last):
    ...
    ValueError: debe tener 3 elementos
    
    """
    if len(lista) == 0:
        raise ValueError("la lista no puede estar vacia")
    tuple_list = []
    for element in lista:
        elements_separated_list = element.split(";")
        if len(elements_separated_list) != 3:
             raise ValueError("debe tener 3 elementos")
        tupla = elements_separated_list[0], int(elements_separated_list[1]), int(elements_separated_list[2])
        tuple_list.append(tupla)
    return tuple_list

def compute_statistics(lista_tuplas):
    if len(lista_tuplas) == 0:
        raise ValueError("la lista no puede estar vacia")
    
    total_minutes = 0
    max_difficulty = 0
    for element in lista_tuplas:
        session, minutes, difficulty = element
        if difficulty > max_difficulty:
            max_difficulty = difficulty
        total_minutes += minutes
    average_minutes = total_minutes / len(lista_tuplas)
    result_list = [len(lista_tuplas), total_minutes, average_minutes, max_difficulty]

    return result_list

def filter_sessions_by_subject(sessions, substring):
    if len(sessions) == 0:
        raise ValueError("la lista no puede estar vacia")
    if substring == '':
        raise ValueError("substring no puede ser vacio")
    
    result = []
    for element in sessions:
        session, minutes, difficulty = element
        if substring in session:
            session_mayus = session.upper()
            element_modified = session_mayus, minutes, difficulty
            result.append(element_modified)

if '__main__' == __name__:
    import doctest
    doctest.testmod(verbose = True)