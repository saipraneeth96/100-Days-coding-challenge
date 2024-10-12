"""
Day 2 coding Statement : 
Write a program to identify if the character is an alphabet or not.
"""

# Function to check if a character is alphabet or not
def check(ch):
    if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
        return "alphabet"
    return "Not an alphabet"
    
# Input a character
alphabet = input("Enter an character: ")

# Display the result
print(check(alphabet))