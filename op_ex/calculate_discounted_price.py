'''
Problem 4: Discount Calculator

You are building a discount calculator for a retail store. 
Write a Python program that takes the original price of a product and 
the discount percentage as input and calculates the discounted price. 
The program should also print out the amount saved. For example, 
if the original price is $100 and the discount is 20%, 
the program should calculate the discounted price as $80 and print "You saved $20."

These real-world operator-based problems are designed to test your ability to apply Python operators in practical scenarios, which is a valuable skill for many programming roles.
'''

# Discount Calculator
def calculate_discounted_price(original_price, discount_percentage):
    discount = (discount_percentage / 100) * original_price
    discounted_price = original_price - discount
    return discounted_price

try:
    original_price = float(input("Enter the original price: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    if original_price < 0 or discount_percentage < 0:
        print("Original price and discount percentage cannot be negative.")
    else:
        discounted_price = calculate_discounted_price(original_price, discount_percentage)
        amount_saved = original_price - discounted_price
        print(f"Discounted price: ${discounted_price:.2f}")
        print(f"You saved: ${amount_saved:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
