"""
Day 59 coding Statement:
Body Mass Index

You are given the height H (in metres) and mass M (in kilograms) of Anusree.The Body Mass Index (BMI) of a person is computed as M/H^2.

Report the category into which Anusree falls, based on his BMI:

Category 1: Underweight if BMI ≤18

Category 2: Normal weight if BMI ∈{19, 20,…, 24}

Category 3: Overweight if BMI ∈{25, 26,…, 29}

Category 4: Obesity if BMI ≥30

SOLUTION:
"""

# input number of testcases
t = int(input())

for i in range(t):
    # m to store mass of person
    # h to store height of person
    m, h  = map(int, input().split())
    # calculate BMI
    bmi = m/h**2
    
    # output the category of the person
    if bmi <= 18:
        print("1")
    elif bmi >= 19 and bmi <= 24:
        print("2")
    elif bmi >= 25 and bmi <= 29:
        print("3")
    elif bmi >= 30:
        print("4")
