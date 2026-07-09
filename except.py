# Program to handle invalid input using try and except

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
