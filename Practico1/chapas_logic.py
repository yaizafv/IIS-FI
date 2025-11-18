
"""
Calcula la nueva posicion hacia la que se desplaza basandose en su posicion original, la velocidad con la que es empujada
y la friccion de la superficie.

Args:
    pos (float): posicion
    speed (float): velocidad
    friction (float): friccion

Returns:
    pos (float): nueva posicion en la que se detiene la chapa

Exception:
    ValueError: args error

Examples:
    >>> move_chapa(0,10,5)
    15
    >>> move_chapa(0,0,1)
    0
    >>> move_chapa(-1,10,2)
    Traceback (most recent call last):
    ...
    ValueError: Player position cannot be negative.
    >>> move_chapa(1,10,0)
    Traceback (most recent call last):
    ...
    ValueError: Friction must be greater than 0


"""
def move_chapa(pos, speed, friction):
    for segundo in range(speed):
         while speed > 0:
            pos += speed
            speed -= friction
            segundo += 1
    return pos

RESULT_PLAYER_1_WINS = 1
RESULT_PLAYER_2_WINS = 2
RESULT_DRAW = 0

"""
Indica el resultado del juego en base a las posiciones finales de cada jugador respecto a la linea de 
meta

Args:
    pos_player1 (float): posicion
    pos_player2 (float): velocidad
    pos_endline (float): friccion

Returns:
    float: 1 if player1 wins, 2 if player2 wins, 0 if draw

Exception:
    ValueError: args incumplen condiciones

Examples:
    >>> solve_game_result(10,5,15)
    1
    >>> solve_game_result(10,15,15)
    2   
    >>> solve_game_result(5,5,15)
    0
    >>> solve_game_result(5,5,0)
    Traceback (most recent call last):
    ...
    ValueError: Finish line position must be greater than 0.
    >>> solve_game_result(-1,3,100)
    Traceback (most recent call last):
    ...
    ValueError: Positions must be greater than or equal to 0.

"""
def solve_game_result(pos_player1, pos_player2, pos_endline):
    distance_end1 = pos_endline - pos_player1
    distance_end2 = pos_endline - pos_player2
    if distance_end1 > distance_end2:
        return RESULT_PLAYER_2_WINS
    elif distance_end1 < distance_end2:
        return RESULT_PLAYER_1_WINS
    else:
        return RESULT_DRAW


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
            
    

