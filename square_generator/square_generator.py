import math

class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of the range cannot be less than the start.")

        squares = [x**2 for x in range(start, end + 1)]
        return squares

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
