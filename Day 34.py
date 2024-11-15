"""
Day 34 coding Statement:
Write a Program to Remove brackets from an algebraic expression

Description:
Get an algebraic expression as input from the user and then remove all the brackets in that.

Input: 7x+(2*y)
Output: 7x+2*y
"""


# input an algebric expression as string
expression = input("Enter an expressionn: ")

# check for brackets and replace them with empty string
for char in ['(',')','[',']','{','}']:
    expression = expression.replace(char, "")
    
# display the result
print(expression)
