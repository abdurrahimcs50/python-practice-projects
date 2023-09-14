
'''
Problem 1: Shipping Calculator

You are tasked with creating a shipping calculator for an e-commerce website. 
Write a Python program that takes the weight of a package as input (in kilograms) 
and calculates the shipping cost based on the following rules:

1. Packages weighing less than 1 kg cost $5 to ship.
2. Packages weighing 1 kg or more but less than 5 kg cost $10 to ship.
3. Packages weighing 5 kg or more but less than 10 kg cost $20 to ship.
4. Packages weighing 10 kg or more cost $30 to ship.
Write a program that takes the package weight as input and calculates the shipping cost.

'''

# Shipping Calculator
def calculate_shipping_cost(weight):
    if weight < 1:
        shipping_cost = 5
    elif weight < 5:
        shipping_cost = 10
    elif weight < 10:
        shipping_cost = 20
    else:
        shipping_cost = 30
    return shipping_cost

# Input: Get the weight of the package from the user
try:
    weight = float(input("What is The Weight Of Your Package (in kg)? "))
    
    # check weight is non-negative
    
    if weight < 0:
        print("Invalid Weight")
    
    else:
        shipping_cost = calculate_shipping_cost(weight)
        print(f"The shipping cost for a {weight} kg package is ${shipping_cost:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid weight (in kilograms).")
    
    
    