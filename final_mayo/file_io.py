def load_sessions(filename):
    contenidos_fichero = []
    try:
        with open(filename, "r") as f:
            line = f.readline()
            while line != "":
                line.strip()
                contenidos_fichero.append(line)
                line = f.readline()
    except FileNotFoundError as fnf:
        print("error buscando fichero: " + fnf)
    return contenidos_fichero

def save_summary(filename, metrics):
    if filename == "":
        raise ValueError("nombre del fichero no puede estar vacío")
    if len(metrics) == 0:
        raise ValueError("la lista esta vacia")
    
    with open(filename, "w") as f:
        total_sessions, total_minutes, average_minutes_per_session, max_difficulty = metrics
        f.write(f"total_sessions {str(total_sessions)} \n")
        f.write(f"total_minutes {str(total_minutes)} \n")
        f.write(f"average_minutes {str(average_minutes_per_session)} \n")
        f.write(f"max_difficulty {str(max_difficulty)} \n")        
                
