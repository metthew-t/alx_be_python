import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for SimpleCalculator class.
    Tests all arithmetic operations with various scenarios including edge cases.
    """
    
    def setUp(self):
        """Set up a fresh calculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test addition operation with various scenarios."""
        # Positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        
        # Negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        
        # Zero cases
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(1.1, 2.2), 3.3)
    
    def test_subtraction(self):
        """Test subtraction operation with various scenarios."""
        # Positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        
        # Negative numbers
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        
        # Zero cases
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(3.3, 1.1), 2.2)
    
    def test_multiplication(self):
        """Test multiplication operation with various scenarios."""
        # Positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)
        
        # Negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Zero cases
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(1.5, 2.5), 3.75)
    
    def test_division(self):
        """Test division operation with various scenarios."""
        # Normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        
        # Decimal results
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(1, 3), 1/3)
        
        # Negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        
        # Division by one and itself
        self.assertEqual(self.calc.divide(7, 1), 7.0)
        self.assertEqual(self.calc.divide(5, 5), 1.0)
        
        # Zero divided by non-zero
        self.assertEqual(self.calc.divide(0, 5), 0.0)
    
    def test_division_by_zero(self):
        """Test division by zero returns None."""
        # Division by zero should return None
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Verify normal division still works
        self.assertEqual(self.calc.divide(10, 2), 5.0)
    
    def test_large_numbers(self):
        """Test operations with large numbers."""
        # Large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calc.subtract(5000000, 2000000), 3000000)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)
        self.assertEqual(self.calc.divide(1000000, 1000), 1000.0)


if __name__ == '__main__':
    # Run the tests
    unittest.main()