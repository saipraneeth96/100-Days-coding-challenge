Day 56 coding Statement:
Write Program to find whether the numbers of an array be made equal

def can_make_equal(arr):
    # Step 1: Normalize each number by dividing out factors of 2 and 3
    def normalize(num):
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        return num

    # Normalize all numbers
    normalized = [normalize(num) for num in arr]

    # Step 2: Check if all normalized values are the same
    if len(set(normalized)) == 1:
        return "Yes"
    else:
        return "No"


size = int(input("Enter size of the array: "))

array = []
# enter elements into array
for i in range(size):
    array.append(int(input()))
    
# Output
print(can_make_equal(array))
