# Ask the user for a temperature in Fahrenheit and convert it to Celsius.

fahrenheit = float(input("Enter the temperature in fahrenheit: "))

celsius = (fahrenheit - 32) * (5 / 9)

print(
    f"{fahrenheit}°F is equal to {celsius}°C")
