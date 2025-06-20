# Ask the user for the radius of a circle and display its area and circumference.

radius = float(input("Enter the radius of the circle: "))

area = (radius * radius) * 3.14
circumference = (radius * 2) * 3.14

print(
    f"The circumference of the circle is: {circumference}, and the area is: {area}")
