"""
Day 42 coding Statement:
Write Program to check if two arrays are the same or not

Description

Get two arrays as the input from the user and check whether it is the same or not.

Input

Enter the size of first array :

3

Enter the size of second array :

3

Enter elements of first array :

1 2 3

Enter elements of second array :

1 2 3

Output

Same
"""


l1 = int(input("Enter the size of first array: "))
l2 = int(input("Enter the size of second array: "))

arr1 = []
for i in range(l1):
    arr1.append(int(input()))
    
arr2 = []
for j in range(l2):
    arr2.append(int(input()))
    
if l1 != l2:
    print("Not Same")
else:
    for k in range(l1):
        if arr1[k] != arr2[k]:
            print("Not Same")
            break
    else:
        print("Same")
