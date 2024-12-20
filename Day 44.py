"""
Day 44 coding Statement:
Write Program to find number of even and odd elements in an array
"""

# input size of array
n = int(input("Enter size of the array: "))

arr = []
# input elements into array
for i in range(n):
    arr.append(int(input()))
    
countOdd, countEven = 0, 0

# count even and odd elements into array
for i in range(n):
    if arr[i] % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
        
print(f"Number of even elements: {countEven}")
print(f"Number of odd elements: {countOdd}")
