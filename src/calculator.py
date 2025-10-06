"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b
def add_negative(a, b):
    """Add the negatives of a and b"""
    return -a + -b  # same as -(a + b)

def subtract_negative(a, b):
    """Subtract the negatives of a and b"""
    return -a - -b  # same as -a + b

import math

def power(a, b):
    """Raise a to the power of b with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    print(f"Calculating {a} ^ {b}")
    result = a ** b
    print(f"Result: {result}")
    return result

def sqrt(a):
    """Calculate the square root of a number with validation and logging."""
    if not isinstance(a, (int, float)):
        raise TypeError("Input must be a number")
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number")
    
    print(f"Calculating √{a}")
    result = math.sqrt(a)
    print(f"Result: {result}")
    return result

def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    print(f"Multiplying {a} × {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
    return result

def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    
    print(f"Dividing {a} ÷ {b}")  # Added logging
    result = a / b
    print(f"Result: {result}")
    return result

# TODO: Students will add multiply, divide, power, sqrt functions

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")