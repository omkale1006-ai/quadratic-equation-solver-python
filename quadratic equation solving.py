# Program to solve a quadratic equation
# The quadratic equation is ax² + bx + c = 0
# a ≠ 0

import math

def solve_quadratic_equation():
    # User input
    a = float(input("Enter coefficient a (a ≠ 0): "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("This is not a quadratic equation because 'a' is zero.")
        return

    # Calculate discriminant
    discriminant = b**2 - 4*a*c

    # Find roots based on discriminant
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("Two Real and Distinct Roots:")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")

    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        print("One Real and Equal Root:")
        print(f"Root: {root}")

    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        print("Two Complex Roots:")
        print(f"Root 1: {real_part} + {imaginary_part}i")
        print(f"Root 2: {real_part} - {imaginary_part}i")

# Call the function
solve_quadratic_equation()
