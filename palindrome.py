# Program to check whether a string is a palindrome

text = input("Enter a string: ")

if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
