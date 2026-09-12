# Ask the user for their weight (kg) and height (m), and display their Body Mass Index (BMI).

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight / (height * height)

print(f"Your bmi is: {bmi:.2f}")
