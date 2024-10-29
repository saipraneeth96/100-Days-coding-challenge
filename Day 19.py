"""
Day 19 coding Statement:
Write a program to identify if the number is Armstrong number or not

Description

Get an input number from user and check whether the given number is an Armstrong number or not.

E.g. Let the number be 1634,

Here 1^4 + 6^4 + 3 ^4 + 4^4 = 1634

Therefore, this is an Armstrong number
"""


# input a number
num = int(input("Enter a number: "))

# find out number of digits in the number
count = 0
temp1 = num
while temp1 != 0:
    count += 1
    temp1 = temp1 // 10
    

# computing Armstrong number
total = 0
temp2 = num
while temp2 != 0:
    # Extract the last digit
    digit = temp2 % 10   
    # Add digit raised to 'count' to 'total'
    total += digit ** count   
    # Remove the last digit
    temp2 = temp2 // 10
    
# Check if the sum equals the original number
if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
