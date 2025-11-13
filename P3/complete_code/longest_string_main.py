def main():
    string_1 = input("Enter the first string: ")
    string_2 = input("Enter the second string: ")
    string_3 = input("Enter the third string: ")

    string_1_length = len(string_1)
    string_2_length = len(string_2)
    string_3_length = len(string_3)

    longest_size = max(string_1_length, string_2_length, string_3_length)
    print(f"The length of the longest string entered is: {longest_size}")

if __name__ == "__main__":
    main()