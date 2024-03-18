import math

class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            print("Error: End of the range cannot be less than the start.")
            return []

        squares = [x**2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots

# Example usage:
generator = SquareGenerator()
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

squares = generator.generate_squares(start, end)
if squares:
    square_roots = generator.calculate_square_roots(squares)
    print("List of squares within the range:", squares)
    print("Square roots of the numbers:", square_roots)
