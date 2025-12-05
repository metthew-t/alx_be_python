class Calculator:
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
    
    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        # Access class attribute
        print(f"Calculation type: {cls.calculation_type}")
        return a * b