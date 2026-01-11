import cards_logic


def run_basic_functionalities():
    card_list = ["spades", "hearts", "diamonds", "clubs", "hearts"]
    print(card_list)

    card_list.append("spades")
    print(card_list)

    other_card_list = card_list

    card = card_list[3]

    other_card_list[0] = card

    print(card_list)
    print(other_card_list)

    new_card_list = []

    new_card_list.append(other_card_list[2])
    new_card_list.append(other_card_list[5])

    print(card_list)
    print(other_card_list)
    print(new_card_list)

    print(len(card_list))
    print(len(other_card_list))
    print(len(new_card_list))


def main():
    run_basic_functionalities()

if __name__ == "__main__":
    main()
