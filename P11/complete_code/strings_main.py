def show_string_characters_indexing(text):
    print("Showing characters using indexing:")
    for index in range(len(text)):
        print(text[index])
    print('------------')

def show_string_characters_foreach(text):
    print("Showing characters using foreach loop:")
    for character in text:
        print(character)
    print('------------')


def main():
    # Base text
    text = 'Celia Melendi Lavandera:Diego Martín Fernández:Francisco Gil Gala:Javier Escalada Gómez:José Villar Flecha:Manuel Quintela Pumares'
    
    # Accessing characters by index
    first_character = text[0]
    print(f'First character: {first_character}')
    # text[0] = 't' Error

    # Iterating over characters
    show_string_characters_indexing(text)
    show_string_characters_foreach(text)

    # Obtaining a list of strings
    teachers = text.split(':')
    print(f'The teacher list is: {teachers}')

    # Dividing further the first teacher's name
    teacher_name_and_surnames = teachers[0].split(' ')
    print(f'The name and surnames of the first teacher are: {teacher_name_and_surnames}')

    # Joining strings with a different separator
    teachers_string = ', '.join(teachers)
    print(f'The teachers of this course are: {teachers_string}')

    position = teachers_string.find('Diego')
    print(f'Position of "Diego" in text: {position}')

    # position = text.index(',')
    # print(f'Position of "," in text: {position}')

    position = text.find(',')
    print(f'Position of "," in text: {position}')

    half_length = len(text) // 2

    first_half = text[:half_length]
    print(f'First half of the text: {first_half}')

    second_half = text[half_length:]
    print(f'Second half of the text: {second_half}')


if __name__ == "__main__":
    main()