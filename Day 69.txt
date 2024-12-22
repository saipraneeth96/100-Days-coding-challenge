Day 69 coding Statement: OOP Inheritance

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
