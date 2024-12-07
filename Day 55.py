"""
Day 55 coding Statement:
Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the sum of maximum scalar product (Dot product) of 2 vectors.

Sample input 1:

4

1 2 3 4

5 6 7 8

Sample output 1:

70

Explanation :

(8*4 + 7*3 + 6*2 + 1*5) = 70

Sample input 2:

4

-1 -2 -3 -4

5 6 -7 -8

Sample output 2:

37

Explanation :

(-4*-8 + -3*-7 + -2*5 + -1*6) = 37
"""

size = int(input("Enter size of arrays: "))

X = []
# enter elements into first array
for i in range(size):
    X.append(int(input()))

Y = []
# enter elements into second array
for i in range(size):
    Y.append(int(input()))
    
dot_product = 0

for i in range(size):
    dot_product = dot_product + (X[i] * Y[i])
    
# display the Fot Product
print(dot_product)
