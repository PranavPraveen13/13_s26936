def generate_squares(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    return squares

# Get user input for the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Validate input
if start > end:
    print("Error: Start value must be less than or equal to end value.")
else:
    squares = generate_squares(start, end)
    print("List of squares within the range:", squares)
