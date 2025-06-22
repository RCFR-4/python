# Ask the user for the total bill and how many people will split it. Show how much each person pays.

total_bill = float(input("Enter the total bill: "))
total_people = int(input("Enter how many people will split the bill: "))

division = total_bill / total_people

print(f"Each person will pay: {division:.2f} ")
