"""
Day 35 coding Statement:
Write a Program to Count the sum of numbers in a string
"""

# input a string
s = input("Enter a string: ")

total = 0

# loop through each character of string
for char in s:
    #check if character is a number
    if char >= "0" and char <= "9":
        # add it to total
        total = total + int(char)
        
# display the result
print(total)
