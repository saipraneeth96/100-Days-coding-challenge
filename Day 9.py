"""
Day 9 coding Statement : 
Write a program to find Number of digits in an integer
"""

# Input an integer
num = int(input("Enter an integer: "))
# count variable to store count of digits
count = 0

# Extract each digit of the number
while num > 0:
    num = num // 10
    count = count + 1 # Increase count for each digit
    
    
# Display the number of digits    
print(count)
