"""
Day 51 coding Statement:
Given an integer array of size N, write a program to sort the array
"""

size = int(input("Enter size of the array: "))

# emter elements into array
array = []
for i in range(size):
    array.append(int(input()))
    
# sort the array using BUBBLE SPRT
for i in range(size):
    for j in range(size-i-1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            
# display sorted array
print("Sorted array: ",array)
