"""
Day 70 coding Statement:
Given an array, rotate the array by one position in clock-wise direction.

Example 1:

Input:

N = 5

A[] = {1, 2, 3, 4, 5}

Output:

5 1 2 3 4

Example 2:

Input:

N = 8

A[] = {9, 8, 7, 6, 4, 2, 1, 3}

Output:

3 9 8 7 6 4 2 1
"""

# input size of the array
n = int(input())

# input elements into array
array = []
for i in range(n):
    array.append(int(input()))
    
# Reverse the entire array
array = array[::-1]
# Reverse the first element (previously the last)
array[:1] = array[:1][::-1]
# Reverse the remaining elements
array[1:] = array[1:][::-1]

# Rotated array
print(array)
