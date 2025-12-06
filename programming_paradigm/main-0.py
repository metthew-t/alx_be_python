import sys
import sys
from robust_division_calculator import safe_divide

def main():
    # Check if exactly 2 arguments are provided (plus script name)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        print("Example: python main.py 10 5")
        print("Example: python main.py 7.5 2")
        sys.exit(1)

    # Get command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform safe division
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()