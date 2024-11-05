"""
Day 25 coding Statement:
Write a program to find Area of a circle

Description:
Get the value for radius from the user and calculate the area of the circle for the given radius.

Area of circle = 3.14*radius*radius

Input: 3

Output: 28.26
"""

# input the radius of circle
radius = float(input("Enter the radius of number: "))

# calculing the area
area = 3.14 * radius * radius

# display the result
print(round(area, 2))
