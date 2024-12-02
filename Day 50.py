"""
Day 50 coding Statement:
Given an integer array of size N. Write Program to find sum of positive square elements in the array.

Sample input 1 :

4 1 2 3 4

Sample output 1 :

30

Explanation :

(1 + 4 + 9 + 16) = 30

Sample input 2 :

4 -1 -2 -3 -4

Sample output 2 :

30

Explanation :

(1 + 4 + 9 + 16) = 30
"""

size = int(input("Enter size of the array: "))

array = []
# enter elements into array
for i in range(size):
    array.append(int(input()))
    
# square the elements of the array
for i in range(len(array)):
    array[i] = array[i]**2
    
# convert list to set to eliminate duplicates
unique = set(array)

# calculate summ of elements of this set
total = sum(unique)

print(total)
