def main():
    print("We are going to encrypt 1 character with Caesar cipher")

    character = input("Enter a character: ")

    character_code = ord(character)

    print(f"The original ASCII code is: {character_code}")

    key_text = input("What encryption key do you want to use? (1-25) ")
    key = int(key_text)
    print(f"Encryption key (shift): {key}")

    encrypted_code = character_code + key

    encrypted_character = chr(encrypted_code)

    print(f"The encrypted ASCII code is: {encrypted_code}")
    print(f"The encrypted character is: {encrypted_character}")

    print("Now we are going to decrypt the character")

    decrypted_code = ord(encrypted_character) - key

    decrypted_character = chr(decrypted_code)

    # We can also do it this way, but it's better to do it in two steps
    decrypted_character = chr(ord(encrypted_character) - key)

    print(f"The decrypted ASCII code is: {decrypted_code}")
    print(f"The decrypted character is: {decrypted_character}")
    


if __name__ == "__main__":
    main()
