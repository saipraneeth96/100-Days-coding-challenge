"""
Day 49 coding Statement:
Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the minimum scalar product (Dot product) of 2 vectors.

Sample input 1 :

4

1 2 3 4

5 6 7 8

Sample output 1 : 60

Explanation : (4*5 + 3*6 + 2*7 + 1*8) = 60

Sample input 2 :

4

-1 -2 -3 -4

5 6 -7 -8

Sample output 2 : -17

Explanation : (-1*-8 + -2*-7 + -3*6 + -4*5) = -17
"""

# input size of arrays
"""assuming both the arrays are of same size"""
size = int(input("Enter size of arrays: "))

# enter elements into arrays
array1, array2 = [], []

print("Elements in first array")
for i in range(0, size):
    array1.append(int(input()))

print("Elements in second array")    
for i in range(0, size):
    array2.append(int(input()))
    
# calculating dot product(scalar product)
dot_product = 0

for i in range(0, size):
    dot_product = dot_product + (array1[i] * array2[size-i-1])
    
# display the result
print("Dot Product: ", dot_product)
