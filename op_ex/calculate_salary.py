'''
Problem 3: Employee Salary Calculator

You are working on an HR system for a company. 
Write a Python program that calculates the monthly salary of an employee based 
on their hourly wage and the number of hours they worked in a month. 
Additionally, if an employee worked more than 40 hours in a week, 
they should receive overtime pay at 1.5 times their hourly wage for 
each hour worked beyond 40 hours. The program should take the hourly wage and 
the number of hours worked as input and calculate the total monthly salary.

'''

# Employee Salary Calculator
def calculate_salary(hourly_wage, hours_worked):
    regular_pay = hourly_wage * min(hours_worked, 40)  # Calculate regular pay for up to 40 hours
    overtime_hours = max(hours_worked - 40, 0)        # Calculate overtime hours (if any)
    overtime_pay = 1.5 * hourly_wage * overtime_hours  # Calculate overtime pay
    total_salary = regular_pay + overtime_pay          # Calculate total salary
    
    return total_salary

try:
    hourly_wage = float(input("Enter hourly wage: $"))
    hours_worked = float(input("Enter hours worked: "))
    
    if hourly_wage < 0 or hours_worked < 0:
        print("Hourly wage and hours worked cannot be negative.")
    else:
        salary = calculate_salary(hourly_wage, hours_worked)
        print(f"Total monthly salary: ${salary:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
