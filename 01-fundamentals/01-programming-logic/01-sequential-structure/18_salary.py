# Ask the user for a salary and the percentage of tax discount. Display the final salary after tax.

salary = float(input("Enter the salary: "))
tax = float(input("Enter the tax percentage: "))

tax_value = salary * (tax / 100)
final_salary = salary - tax_value


print(f"The final salary after tax is:{final_salary:.2f}")
