"""
Day 54 coding Statement:
Given an integer array of size N. Write Program to find whether Arrays are disjoint or not. 
Two arrays are said to be disjoint if they have no elements in common.

Sample input 1:

4

2 -4 -1 -3

3

1 3 5

Sample output 1:

Disjoint

Sample input 2:

5

1 5 -7 6 3

4

2 4 6 8

Sample output 2:

Not disjoint. ( 6 is common)
"""

# function to check if arrays are disjoint
def joint(array1, array2):
    for num in array1:
        if num in array2:
            return False
    return True        


size1 = int(input("Enter size of first array: "))

array1 = []
print("Elements of first array")
for i in range(size1):
    array1.append(int(input()))
    
size2 = int(input("Enter size of second array"))

array2 = []
print("Elements of second array")
for i in range(size2):
    array2.append(int(input()))

if joint(array1, array2):
    print("Disjoint")
else:
    print("Not Disjoint")
