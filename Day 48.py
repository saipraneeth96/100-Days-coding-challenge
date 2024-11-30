"""
Day 48 coding Statement:
Write Program to remove duplicate elements in an array
"""


# input size of the array
size = int(input("Enter size of the array: "))

# add elements to the array
array = []
print("Original array")
for i in range(size):
    array.append(int(input()))
    
new_array = []    
# iterate through each element of the array
for element in array:
    # add element to new_array if it is not present 
    if element not in new_array:
        new_array.append(element)
        
print("Array after removing duplicates")        
for i in range(len(new_array)):
    print(new_array[i])
