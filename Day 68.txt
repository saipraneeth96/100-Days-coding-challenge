Day 68 coding Statement:
You will be given queries. Each query is of one of the following three types: :

# Read the number of queries
num_queries = int(input())

# Initialize an empty set
my_set = set()

# Process each query
for i in range(num_queries):
    query = input().split()
    query_type = int(query[0])
    value = int(query[1])
    
    if query_type == 1:  # Add value to the set
        my_set.add(value)
    elif query_type == 2:  # Delete value from the set
        my_set.discard(value)  # Using discard avoids errors if value is not in the set
    elif query_type == 3:  # Check if value is in the set
        if value in my_set:
            print("Yes")
        else:
            print("No")
