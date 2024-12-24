"""
Day 72 coding Statement:
In this problem, you will have to implement a simple editor. The editor maintains the content of a string S and have two following functions

"+ i x": insert a string x into the current string S after the i'th character of the S (we use 1-indexing in this problem).
When i equals to 0 it mean we add x at the beginning of S.
"? i len": Print the sub-string of length len starting at position i'th of S.
At the beginning, the editor holds an empty string. There will be Q queries of the two types described above.

Input

The first line contains the integer Q. Each line in the next Q lines contains one query.

Output

For each query of the second type, print out the answer sub-string in one line.

Sample Input

5

+ 0 ab

+ 1 c

? 1 3

+ 2 dd

? 1 5

Sample Output

acb

acddb
"""

# Function to process queries
def process_queries(queries):
    # Initialize the string S
    S = ""
    
    # Results for '? i len' queries
    results = []

    # Process each query
    for query in queries:
        parts = query.split()
        
        if parts[0] == '+':
            # Extract the parameters for the `+` query
            i = int(parts[1])  # Position
            x = parts[2]       # String to insert
            
            # Insert x at the i-th position (1-indexed)
            S = S[:i] + x + S[i:]
        
        elif parts[0] == '?':
            # Extract the parameters for the `?` query
            i = int(parts[1])  # Start position
            length = int(parts[2])  # Length of the substring
            
            # Extract the substring (1-indexed)
            result = S[i-1:i-1+length]
            results.append(result)

    return results



# Input reading
Q = int(input())
queries = [input().strip() for i in range(Q)]

# Process queries and output results
results = process_queries(queries)
for res in results:
    print(res)
