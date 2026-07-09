# Function to check whether a number is prime

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# Main program
number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a Prime number.")
else:
    print(number, "is not a Prime number.")
