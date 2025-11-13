import areas_logic
import user_io


def main():
    """Main function."""
    side_length = user_io.ask_positive_integer("Introduce the square side length: ")
    square_area = areas_logic.calculate_square_area(side_length)
    print(f'The square_area is {square_area}')
    
    rectangle_width = user_io.ask_positive_integer("Introduce the rectangle width: ")
    rectangle_height = user_io.ask_positive_integer("Introduce the rectangle height: ")
    rectangle_area = areas_logic.calculate_rectangle_area(rectangle_height, rectangle_width)
    print(f'The rectangle area is {rectangle_area}')
    
    base_length = user_io.ask_positive_integer("Introduce the triangle base length: ")
    height_length = user_io.ask_positive_integer("Introduce the triangle height length: ")
    triangle_area = areas_logic.calculate_triangle_area(base_length, height_length)
    print(f'The triangle area is {triangle_area}')


if __name__ == "__main__":
    main()
