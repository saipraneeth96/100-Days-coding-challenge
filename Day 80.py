"""
Day 80 coding Statement : 

Alice and Bob went to a pet store. There are N animals in the store where the ith animal is of type Ai?.
Alice decides to buy some of these N animals. Bob decides that he will buy all the animals left in the store after Alice has made the purchase.
Find out whether it is possible that Alice and Bob end up with exactly same multiset of animals.

Input Format

The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains an integer N — the number of animals in the store.
The next line contains N space separated integers, denoting the type of each animal.
Output Format

For each test case, output on a new line, YES, if it is possible that Alice and Bob end up with exactly same multiset of animals and NO otherwise.

You may print each character in uppercase or lowercase. For example, the strings YES, yes, Yes, and yES are considered identical.


Sample Input

4
3
4 4 4
4
2 3 3 2
4
1 2 2 3
6
5 5 1 5 1 5

Sample Output

NO
YES
NO
YES

"""

def multiset(n, nums):
    # dictionary to store count of each animal type
    freq = {}
    
    for i in range(n):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
            
    for key, value in freq.items():
        if value % 2 != 0:
            return "NO"
            
            
    return "YES"        


# input number of test cases
t = int(input())

for i in range(t):
    # input number of animals in the store
    N = int(input())
    
    # input type of animal
    animals = list(map(int, input().split()))
    
    result = multiset(N, animals)
    
    # print the output
    print(result)
