"""
Day 95 coding Statement : 

Kulyash is given an integer N. His task is to break N into some number of (integer) powers of 2.

To achieve this, he can perform the following operation several times (possibly, zero):

Choose an integer X which he already has, and break X into 2 integer parts (Y and Z) such that X=Y+Z.
Find the minimum number of operations required by Kulyash to accomplish his task.

Input Format

The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line of input.
The first and only line of each test case contains an integer N — the original integer with Kulyash.
Output Format

For each test case, output on a new line the minimum number of operations required by Kulyash to break N into powers of 2.

 

Sample Input

2

3

4

Sample Output

1

0

"""

def min_operations_to_powers_of_2(N):
    # Count the number of 1's in binary representation of N
    num_of_ones = bin(N).count('1')
    # Minimum operations is number of 1's - 1
    return num_of_ones - 1

# Input reading
T = int(input("Enter number of test cases: "))

for i in range(T):
    N = int(input("Enter N: "))

    # Process and Output
    results = min_operations_to_powers_of_2(N)
    print(results)
