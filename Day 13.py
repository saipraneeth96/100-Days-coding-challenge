"""
Day 13 coding Statement:
Write a program to find Sum of N natural numbers
"""


# Input the limit of natural numbers
num = int(input("Enter value of n: "))

# Variable to store sum
sum = 0

# Calculate the sum
for i in range(1, num+1):
    sum = sum + i
    
# Display the result    
print(sum)    
