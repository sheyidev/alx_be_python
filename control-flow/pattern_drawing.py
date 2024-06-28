## Create a Python script named multiplication_table.py. This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.
number = int(input("Enter the size of the pattern: "))

row = 0
while row < number:
    for col in range(number):
        print("*", end="")
    print()
    row += 1