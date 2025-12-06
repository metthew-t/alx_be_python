def saf_Division(numerator, denominator):

    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return f"Error: please provide numeric values"
    try:
        result = num / den
        if result.is_integer():
            return F"the result is {int(result)}"
        else:
            return f"the result is {result}"
    except ZeroDivisionError:
        return "Error: division by zero is not allowed"
    



    import sys
    from library_management import save_Division

    def main():
        if len(sys.argv) != 3:
            print("Usage:python main.py <numerator> <denominator>")
            print("Example1: python main.py 10 2")
            print("Example2: python main.py 14 8")
            sys.exit(1)
        
        numerator = sys.argv[1]
        denominator = sys.argv[2]
        result = saf_Division(numerator, denominator)
        print(result)
    
    if __name__ == "__main__":
        main()