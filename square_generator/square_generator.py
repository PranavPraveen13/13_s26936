from abc import ABC, abstractmethod
import math

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):

        pass

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of the range cannot be less than the start.")

        squares = [x**2 for x in range(start, end + 1)]
        return squares

    def generate_cubes(self, start, end):

        if end < start:
            raise ValueError("End of the range cannot be less than the start.")

        cubes = [x**3 for x in range(start, end + 1)]
        return cubes

# Example usage:
generator = CubicGenerator()
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

squares = generator.generate_squares(start, end)
if squares:
    square_roots = generator.calculate_square_roots(squares)
    print("List of squares within the range:", squares)
    print("Square roots of the numbers:", square_roots)
