"""
Day 40 coding Statement:
Write a Program to Replace substring in a string

Description
Get a string as input from the user and then get another string which has to be removed from the string.
Get the third input, the new substring which is placed in that substring position.
Finally print the output by replacing the substring with new string.

Input

Enter a string: talentbattle

Enter the substring to be removed: talent

Enter the new substring: student

Output

The new string: studentbattle

"""


# input a string
text = input("Enter a string: ")

# input substring to be removed
sub1 = input("Enter the substring to be removed: ")

# input substring to be added
sub2 = input("Enter the new substring: ")

# remove sub1 from text and sub2
modified_string = text.replace(sub1, sub2)
    
# display the result
print(modified_string)

