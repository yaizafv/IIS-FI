def ask_user_option():
    condition = True
    while condition:
        try:
            option = input("Introduce una opcion: ")
            if option != " ":
                condition = False
        except IOError as e:
                print("se ha detectado un error " + e)
    return option

def ask_user_filename():
    condition = True
    while condition:
        try:
            filename = input("Introduce nombre del fichero: ")
            if filename != "":
                condition = False
        except IOError as e:
            print("se ha detectado un error " + e)
    return filename

def ask_user_filename_output():
    condition = True
    while condition:
        try:
            filename = input("Introduce nombre del fichero para guardar los resultados: ")
            if filename != "":
                condition = False
        except IOError as e:
            print("se ha detectado un error " + e)
    return filename

def ask_substring():
    condition = True
    while condition:
        try:
            substring = input("Introduce una subcadena: ")
            if substring != "":
                condition = False
        except IOError as e:
            print("se ha detectado un error " + e)
    return substring