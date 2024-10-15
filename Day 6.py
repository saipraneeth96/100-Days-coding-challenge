"""
Day 6 coding Statement:
Write a program to find the Quadrants in which coordinates lie
"""


# Input X and Y coordinates
x = int(input("Enter X coordinate: "))
y = int(input("Emter Y coordinate: "))

if x > 0 and y > 0:
    print("The point lie in First quadrant")
elif x < 0 and y > 0:
    print("The point lie in Second quadrant")
elif x < 0 and y < 0:
    print("The point lie in Third quadrant")
elif x > 0 and y < 0:
    print("The point lie in Fourth quadrant")
else:
    print("The point is doesn't lie in any quadrant")
