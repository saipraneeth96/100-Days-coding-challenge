"""
Day 7 coding Statement:  
Write a program to find Number of days in a given month of a given year
"""


# Input month and year 
month = int(input("Enter month: "))
year = int(input("Enter year: "))


# Function to check if year is leap year
def leap(year):
    if year%100 == 0 and year%100 == 0:
        return True
    elif year%4 == 0 and year%100 != 0:
        return True
    else:
        return False


# output number of days based on year and month        
if month in [1,3,5,7,8,10,12]:
    print("31")
elif month in [4,6,9,11]:
    print("30")
elif month == 2 and leap(year) == True:
    print("29")
elif month == 2 and leap(year) == False:
    print("28")
else:
    print("Invalid month")
