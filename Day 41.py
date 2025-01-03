"""
Day 41 coding Statement:
Check if two strings match where one string contains wildcard characters

Description
Get two strings as input from the user, first with wildcard characters (* and ?) and second without wildcard characters.
Then check whether they match or not.

Input:

Ta**nt
Talent

Output: Yes they match

"""



# Input a string with wildcard characters
str1 = input("Enter string with wildcards (* or ?): ")

# Input string without wildcard characters
str2 = input("Enter string without wildcards: ")

if len(str1) == len(str2):
    l1 = list(str1)
    l2 = list(str2)

    match = True  # Flag to track whether they match
    for i in range(len(l1)):
        if l1[i] == "*" or l1[i] == "?":
            continue
        elif l1[i] != l2[i]:
            match = False
            print("They do not match")
            break

    if match:  # Only print if the strings match
        print("Yes, they match")

else:
    print("They do not match")
