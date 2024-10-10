"""
Day 1 coding Statement: 
Write a program to identify if the character is a vowel or consonant.
"""

# Function to check if an alphabet is vowel or consonant
def check(alphabet):
    vowels = "aeiouAEIOU"
    if alphabet in vowels:
        return "Vowel"
    else:
        return "Consonant"
        
# Input a character
alphabet = input("Enter a character: ")

# Check if input is an alphabet
if alphabet.isalpha():
    print(check(alphabet))
else:
    print("Invalid Entry!")
