"""
Day 52 coding Statement:
Given an integer array of size N, write a program to reverse the array.
"""

size = int(input("Enter size of the array: "))

# enter elements into array
array = []
for i in range(size):
    array.append(int(input()))
    
# swap elements of array from similar positions from first and last
for i in range(size//2):
    temp = array[i]
    array[i] = array[size-1-i]
    array[size-1-i] = temp
    
# the reversed array
print("Reversed array: ", array)
