"""
Day 68 coding Statement:

You will be given queries. Each query is of one of the following three types: :
Add an element to the set. :
Delete an element from the set. (If the number is not present in the set, then do nothing). :
If the number is present in the set, then print "Yes"(without quotes) else print "No"(without quotes).

Input Format

The first line of the input contains where is the number of queries.
The next lines contain query each. Each query consists of two integers and where is the type of the query and is an integer.

Output Format

For queries of type print "Yes"(without quotes) if the number is present in the set and if the number is not present, then print "No"(without quotes).
Each query of type should be printed in a new line.

Sample Input

8
1 9
1 6
1 10
1 4
3 6
3 14
2 6
3 6

Sample Output

Yes
No
No

"""



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
