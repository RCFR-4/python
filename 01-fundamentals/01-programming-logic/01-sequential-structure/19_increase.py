# Ask the user for a product price and the percentage of increase. Display the new price.

product = float(input("Enter the price of the product: "))
increase = float(input("Enter the increase percentage: "))

increase_value = product * (increase / 100)
final_price = product + increase_value

print(f"the price of the product after the increase is: {final_price}")
