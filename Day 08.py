"""
Day 8 coding Statement:  
Write a program to find roots of a quadratic equation
"""


#Importing math library
import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


# calculating delta
delta = b**2 - 4*a*c

# checking for imaginary roots
if delta < 0:
    print("Roots are imaginary")

# otherwise calculate the roots
else:
    p = ((-1)*b) + math.sqrt(delta)
    q = ((-1)*b) - math.sqrt(delta)

    root1 = p / (2*a)
    root2 = q / (2*a)

    print(f"Root 1 = {root1}")
    print(f"Root 2 = {root2}")
