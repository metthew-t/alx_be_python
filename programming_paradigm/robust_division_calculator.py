def safe_divide(numerator, denominator):
    
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
    
    try:
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    
    