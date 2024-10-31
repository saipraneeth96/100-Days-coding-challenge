"""
Day 21 coding Statement:
Write a program to identify if the number is Palindrome or not
"""


# reverse the input number
def change(num):
    rev = 0
    while num != 0:
        temp = num % 10
        rev = rev*10 + temp
        num = num // 10
    return rev    


# input a number
num = int(input("Enter a number: "))

# check for palindrome
if change(num) == num:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
