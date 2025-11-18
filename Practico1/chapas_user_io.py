def ask_speed():
    condition = True
    while condition:
        try:
            speed = int(input("Introduce la velocidad a la que vas a lanzar la chapa en un rango de (0, 20]: "))
            if speed > 0 and speed <= 20:
                    condition = False
        except ValueError as e:
            print(e)
    return speed