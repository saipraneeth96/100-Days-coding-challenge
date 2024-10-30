"""
Day 20 coding Statement:
Write a program to identify if the number is Prime number or not
"""


# function to check if number is prime or not
def prime(num):
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            return False
    return True    
    
# input a number    
num = int(input("Enter a number: "))

# display the result
if prime(num):
    print("Prime number")
else:
    print("Nota prime number")
