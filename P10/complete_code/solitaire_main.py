import solitaire_cards
import solitaire_logic
import solitaire_user_io

PAIRS_SCORE = 1
POKER_SCORE = 5
COLOR_FLUSH_SCORE = 7
FLUSH_SCORE = 4
COLOR_SCORE = 3

def count_score(columns):
    pairs = 0
    pokers = 0
    color_flushes = 0
    flushes = 0
    colors = 0
    
    for column in columns:
        pairs += solitaire_logic.count_pairs(column)
        pokers += solitaire_logic.count_pokers(column)
        color_flushes += solitaire_logic.count_color_flush(column)
        flushes += solitaire_logic.count_flush(column)
        colors += solitaire_logic.count_color(column)


    total_score = (
        pairs * PAIRS_SCORE +
        pokers * POKER_SCORE +
        color_flushes * COLOR_FLUSH_SCORE +
        flushes * FLUSH_SCORE +
        colors * COLOR_SCORE
    )

    return total_score


def game_loop():
    shuffled_deck = solitaire_cards.create_shuffled_deck()

    columns = solitaire_logic.create_columns(shuffled_deck, 3)

    for _ in range(3):
        solitaire_user_io.show_columns(columns)
        origin_position, destination_position = solitaire_user_io.ask_move(columns)
        columns = solitaire_logic.move_card(
            columns, origin_position, destination_position
        )

    total_score = count_score(columns)

    print(f'Your total score is: {total_score}')

def main():
    game_loop()


if __name__ == "__main__":
    main()