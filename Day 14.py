"""
Day 14 coding Statement:
Write a program to reverse a given number
"""


# Input a number
num = int(input("Enter a number: "))

i, reverse = 0, 0

while num != 0:
    # Extract the last digit of num
    temp = num % 10
    # Add it it reverse based on digit's position
    reverse = reverse * 10 + temp
    # Increment the digit position
    i = i+1
    # Update num by removing last present digit
    num = num // 10
    
# Display the result    
print(reverse)    
