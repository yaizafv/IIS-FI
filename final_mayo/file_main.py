import file_io
import file_logic
import file_user_io

OPTION_SESSION = "1"
OPTION_METRICS = "2"
OPTION_FILTER_SESSION_PER_SUBSTRING = "3"

def show_menu():
    print(f"Leer sesiones desde un fichero: {OPTION_SESSION}")
    print(f"Calcular métricas: {OPTION_METRICS}")
    print(f"Filtrar sesiones por subcadena: {OPTION_FILTER_SESSION_PER_SUBSTRING}")

def handle_option(option):
    if option == OPTION_SESSION:
        filename = file_user_io.ask_user_filename()
        file_io.load_sessions(filename)
    elif option == OPTION_METRICS:
        filename = file_user_io.ask_user_filename()
        list = file_io.load_sessions(filename)
        list_tuplas = file_logic.parse_sessions(list)
        result = file_logic.compute_statistics(list_tuplas)
        filename_to_save = file_user_io.ask_user_filename_output()
        file_io.save_summary(filename_to_save, result)
        print(result)
    elif option == OPTION_FILTER_SESSION_PER_SUBSTRING:
        filename = file_user_io.ask_user_filename()
        list = file_io.load_sessions(filename)
        list_tuplas = file_logic.parse_sessions(list)
        result = file_logic.compute_statistics(list_tuplas)
        substring = file_user_io.ask_substring()
        result_filter = file_logic.filter_sessions_by_subject(result, substring)
        print(result_filter)

def main():
    show_menu()
    option = file_user_io.ask_user_option()
    handle_option(option)

if '__main__' == __name__:
    main()

