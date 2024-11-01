"""
Day 22 coding Statement:
Write a program to express a number as a sum of two prime numbers
"""



# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+ 1):
        if num % i == 0:
            return False
    return True

# Function to find two prime numbers that sum up to the given number
def express_as_sum_of_primes(n):
    for i in range(2, (n // 2) + 1):
        if is_prime(i) and is_prime(n - i):
            return [i, n - i]

# Input from the user
number = int(input("Enter a number: "))

# Find and display the result
result = express_as_sum_of_primes(number)
if result:
    print(f"{number} can be expressed as the sum of {result[0]} and {result[1]}")
else:
    print(f"{number} cannot be expressed as a sum of two prime numbers.")
