"""
Day 11 coding Statement:
Write a program to find Fibonacci series up to n
"""


# Input the limit of fibonacci series
n = int(input("Enter number of terms in series: "))

# Initialize list with initial two terms
fibo = [0,1]

if n == 1:
    print(fibo[0])
if n == 1:
    print(fibo)
else:
    for i in range(0, n-2):
        fibo.append(fibo[-1] + fibo[-2])
    print(fibo)