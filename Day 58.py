
Day 58 coding Statement : Bucket Filling

Nejiya has a bucket having a capacity of K liters. It is already filled with X liters of water.

Find the maximum amount of extra water in liters that Nejiya can fill in the bucket without overflowing.

SOLUTION:

# input number of test cases
t = int(input("Number of test cases: "))

for i in range(t):
    k, x = map(int, input().split())
    # k = total capacity of bucket
    # x = filled amount
    # remaining amount = k - x
    print(k-x)
