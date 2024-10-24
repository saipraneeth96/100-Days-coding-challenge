"""
Day 15 coding Statement:
Write a program to identify if the number is Strong number or not

Get a number as input from user and then check whether that number is a strong number or not. A number is said to be strong number if the sum of the factorial of each digit in the number is same as that of the number.

E.g. let the number be 145

Here 1! + 4! + 5! is 1 + 24 + 120 which is equal to 145 itself.

Input

121

Output

Not a strong number
"""


# Function to calculate factorial of a number
def fact(n):
    # Initialize product to 1
    product = 1
    # Loop from n down to 1 to calculate factorial
    for i in range(n, 0, -1):
        product = product * i
    return product
    
    
# Function to extract digits and calculate sum of their factorial
def strong(num):
    # Initialize total to store sum of factorials of digits
    total = 0
    # loop until all digits are processed
    while num != 0:
        # Get the last digit of num
        temp = num % 10
        # Add the factorial of the digit to total
        total = total + fact(temp)
        # Remove the last digit from num
        num = num // 10
        
    return total
    
# input the number    
num = int(input("Enter a number: "))

# check if it is a strong number or not
if strong(num) == num:
    print("Strong")
else:
    print("Not Stromg")
