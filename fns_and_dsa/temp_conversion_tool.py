# Define Global Conversion Factors:
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Implement Conversion Functions:
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User Interaction:
temp_input = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

# If the user entered a wrong input, raise an error
try:
    temperature = float(temp_input)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

if unit.upper() == 'F':
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")
elif unit.upper() == 'C':
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F")
else:
    print("Invalid unit entered.")