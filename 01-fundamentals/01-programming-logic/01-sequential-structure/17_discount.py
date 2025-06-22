# Ask the user for the price of a product and a discount percentage, and show the discounted price.

price_total = float(input("Enter the price of the product: "))
discount = float(input("Enter the discount percentage: "))

valor_discount = price_total * (discount / 100)
final_price = price_total - valor_discount

print(f"The final price of product with the discount is: {final_price:.2f}")
