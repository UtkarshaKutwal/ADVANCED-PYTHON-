# Program to find the largest element in a list

numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

largest = max(numbers)

print("The largest element in the list is:", largest)
