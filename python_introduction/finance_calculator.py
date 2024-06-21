## Task Description:
"""
You will create a script named finance_calculator.py. 
This script will calculate the user’s monthly savings based on inputted monthly income and expenses. 
It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.
"""
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")