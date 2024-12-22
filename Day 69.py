"""
Day 69 coding Statement: OOP Inheritance

Suppose, we have a class A which is the base class and we have a class B which is derived from class A and we have a class C which is derived from class B,
we can access the functions of both class A and class B by creating an object for class C.
Hence, this mechanism is called multi-level inheritance. (B inherits A and C inherits B.)
Create a class called Equilateral which inherits from Isosceles and should have a function such that the output is as given below.

Sample Output

I am an equilateral triangle
I am an isosceles triangle I am a triangle

"""

# Base class
class Triangle:
    def __init__(self):
        pass

    def print_triangle(self):
        print("I am a triangle")

# Derived class from Triangle
class Isosceles(Triangle):
    def __init__(self):
        super().__init__()

    def print_isosceles(self):
        print("I am an isosceles triangle")

# Derived class from Isosceles
class Equilateral(Isosceles):
    def __init__(self):
        super().__init__()

    def print_equilateral(self):
        print("I am an equilateral triangle")

# Object of class Equilateral
obj = Equilateral()

# Calling the functions
obj.print_equilateral()
obj.print_isosceles()
obj.print_triangle()
