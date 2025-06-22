# Ask the user for a temperature in Celsius and convert it to Fahrenheit.

celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = (celsius * (9 / 5)) + 32

print(
    f"{celsius}°C is equal to {fahrenheit}°F")
