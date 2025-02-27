"""
\Day 43 coding Statement:
Write Program to find the array type

Description: Get an array as input from the user and check the type of the array, whether it is odd, even or mixed type.

Input

Enter size of array : 3

Enter elements 
1 3 5

Output: Odd
"""

# input size of the array
n = int(input("Enter size of the array: "))

arr = []
# input elements into the array
for i in range(n):
    arr.append(int(input()))

count1, count2 = 0, 0
# check if elements in array are odd or even    
for i in range(n):
    if arr[i] % 2 == 0:
        count1 += 1
    else:
        count2 += 1
# if all elements in the array are even
if count1 == n:
    print("Even")
# if all elements in the array are odd
elif count2 == n:
    print("Odd")
# if elements in the array are of both even and odd    
else:
    print("Mixed")
