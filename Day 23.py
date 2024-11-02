"""
Day 23 coding Statement:
Write a program to Replace all 0’s with 1 in a given integer
"""


# input a number
num = int(input("Enter a number: "))

# convert the integer to string
new = str(num)

# empty string to store the result
result = ""

# loop through each character of the string
for x in new:
    if x == "0":
        # Replace '0' with '1'
        result += "1"
    else:
        # Keep the original character
        result += x

# This will display the modified number as a string
print(result)
