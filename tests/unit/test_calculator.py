"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import (
    add, subtract, add_negative, subtract_negative,
    multiply, divide, power, sqrt
)

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    # Negative numbers tests
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add_negative(2, 3) == -5
        assert add_negative(10, 15) == -25

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract_negative(5, 3) == -2
        assert subtract_negative(10, 4) == -6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)
        with pytest.raises(ValueError, match="Cannot divide 10 by zero"):
            divide(10, 0)

class TestPowerSqrtOperations:
    """Test power and square root functions with validation."""

    def test_power_numbers(self):
        """Test power function with valid numbers"""
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(4, 0.5) == 2.0  # sqrt using fractional exponent

    def test_power_input_validation(self):
        """Test power rejects non-numeric inputs"""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power("2", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power(2, "3")

    def test_sqrt_numbers(self):
        """Test sqrt function with valid numbers"""
        assert sqrt(16) == 4.0
        assert sqrt(0) == 0.0

    def test_sqrt_input_validation(self):
        """Test sqrt rejects invalid inputs"""
        with pytest.raises(TypeError, match="Input must be a number"):
            sqrt("16")
        with pytest.raises(ValueError, match="Cannot compute square root of a negative number"):
            sqrt(-4)
