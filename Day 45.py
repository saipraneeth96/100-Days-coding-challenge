"""
Day 45 coding Statement:
Write Program to find smallest and largest element in an array
"""

# input size of the array
n = int(input("Enter size of the array: "))

arr = []
# input elements into array
for i in range(n):
    arr.append(int(input()))
    
"""
everytime we find an element > maxi, 
update maxi with this element
and similarly, everytime we find an element < mini,
update mini with this element.
"""

mini, maxi = arr[0], arr[0]

for i in range(n):
    if arr[i] > maxi:
        maxi = arr[i]
    if arr[i] < mini:
        mini = arr[i]
        
print("Smallest element:", mini)
print("Largest element: ", maxi)
