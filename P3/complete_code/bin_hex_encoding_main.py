def main():
    number_text = input("Enter an integer number: ")
    number = int(number_text)

    digit_count = len(number_text)

    bin_number = bin(number)
    hex_number = hex(number)

    print(f'The number you introduced is {number} and has {digit_count} digits')
    print(f'The binary representation is: {bin_number}')
    print(f'The hexadecimal representation is: {hex_number}')

if __name__ == "__main__":
    main()
