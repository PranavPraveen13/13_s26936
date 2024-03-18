from square_generator.square_generator import SquareGenerator
from square_generator.square_generator import CubicGenerator
# Example usage:

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

generator = SquareGenerator()
squares = generator.generate_squares(start, end)
if squares:
    square_roots = generator.calculate_square_roots(squares)
    print("List of squares within the range:", squares)
    print("Square roots of the numbers:", square_roots)

cubic_generator = CubicGenerator()
cubes = cubic_generator.generate_cubes(start, end)
if cubes:
    print("List of cubes within the range:", cubes)
