FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    # User interaction
    temp_input = input("Enter the temperature to convert: ")
    
    # Implementation of Value Error
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    
    if unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    elif unit == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()