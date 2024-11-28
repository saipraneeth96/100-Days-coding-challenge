"""
Day 46 coding Statement:
Write Program to find sum of elements in an array
"""

# input size of array
n = int(input("Enter size of array: "))

arr = []
# input elements into array
for i in range(n):
    arr.append(int(input()))
    
total = 0
# add each element to total by iterating through the array
for i in range(n):
    total += arr[i]
    
# display the output
print(total)
