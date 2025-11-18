# When documenting doctest cases, these are the first two lines to indicate exceptions:
# Traceback (most recent call last):
# ...
import chapas_logic
import chapas_user_io as user_io


def handle_player_throw(player, player_position, friction):
    """Function that manages the user interaction for throwing a chapa.
    Prints the current position. Requests the user to introduce the speed to throw the capa.
    Moves the chapa and obtains its new position. Prints the new position for the chapa. Returns the new position.
    """
    if player_position < 0:
        raise ValueError('Player position cannot be negative.')
    
    if friction <= 0:
        raise ValueError('Friction must be greater than 0.')

    print(f'---{player} is in position {player_position} and is going to throw---')
    
    speed = user_io.ask_speed()
    
    new_position = chapas_logic.move_chapa(player_position, speed, friction)
    
    print(f'{player} was in position {player_position}, threw at a speed of {speed} and ended in position {new_position}')
    
    return new_position

def show_game_result(player_1_position, player_2_position, finish_line_position):
    """Function to show the game result once it finishes."""
    if player_1_position < 0 or player_2_position < 0:
        raise ValueError('Positions must be greater than or equal to 0.')

    if finish_line_position <= 0:
        raise ValueError('Finish line position must be greater than 0.')
    
    print('------------Game Results------------')
    print(f'Player 1 ended in position {player_1_position}, player 2 in {player_2_position} and the finish line was in {finish_line_position}')
  
    result = chapas_logic.solve_game_result(player_1_position, player_2_position, finish_line_position)
    
    if result == 0: # <----- This value can be changed for a constant.
        print('There has been a DRAW')
    elif result == 1: # <----- This value can be changed for a constant.
        print('Player 1 wins.')
    elif result == 2: # <----- This value can be changed for a constant.
        print('Player 2 wins.')
    else: 
        raise ValueError('Unexpected result.')




#################################################################
#               define the function run_game                    #
#################################################################
# Write the function here
# ValueError: ...
def run_game(player1, player2, finish_line_pos, friction, turns):
    player_position = 0     # empieza en 0
    turno = 1
    while turns > 0:
        print(f"Turno numero {turno}")
        player_1_pos = handle_player_throw(player1, player_position, friction)
        player_2_pos = handle_player_throw(player2, player_position, friction)
        turno += 1
        turns -= 1
    show_game_result(player_1_pos, player_2_pos, finish_line_pos)




def main():
    """Main function. Launches the game."""
    #################################################################
    # start the game with finish line 100, friction 2 and 3 turns   #
    #################################################################
    run_game("Yaiza", "Marcos", 100, 2, 3)
    pass # Remove this line and add your code.


if __name__ == '__main__':
    main()