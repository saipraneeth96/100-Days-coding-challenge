Day 53 coding Statement:
Given an integer array of size N. Write Program to find maximum product subarray in a given array.


# Input size of the array
size = int(input("Enter size of the array: "))

# Input elements into the array
print("Enter elements of the array: ")
array = list(map(int, input().split()))

# Ensure input size matches the array size
if len(array) != size:
    print("Error: The number of elements entered does not match the specified size.")
else:
    # Initializing result to a very small value and tracking subarray
    result = array[0]
    max_subarray = [array[0]]

    for i in range(size):
        mul = 1
        temp_subarray = []
        
        # Traversing in current subarray
        for j in range(i, size):
            mul *= array[j]
            temp_subarray.append(array[j])
            
            # Updating result and subarray if a new maximum is found
            if mul > result:
                result = mul
                max_subarray = temp_subarray[:]
    
    # Display the maximum subarray and its product
    print("Maximum subarray:", max_subarray)
    print("Maximum subarray product:", result)
