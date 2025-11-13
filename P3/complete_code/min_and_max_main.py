def main():
    value_1_text = input("Enter the first value: ")
    value_1 = int(value_1_text)

    value_2_text = input("Enter the second value: ")
    value_2 = int(value_2_text)

    value_3_text = input("Enter the third value: ")
    value_3 = int(value_3_text)

    minimum = min(value_1, value_2, value_3)
    maximum = max(value_1, value_2, value_3)
    difference = maximum - minimum

    print(f"The minimum value is: {minimum}")
    print(f"The maximum value is: {maximum}")
    print(f"The difference between the maximum and minimum values is: {difference}")

if __name__ == "__main__":
    main()