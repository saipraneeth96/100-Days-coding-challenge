"""
Day 26 coding Statement:
Write a program to calculate Maximum number of handshakes

Description:
Get the number of people in the room as input from the user. Then calculate the maximum number of handshakes possible among that people.

For e.g. If there are N people in the room then the first person has to shake hand with N-1 people and second person has to shake hand with N-1-1 people i.e., N-2 handshakes are possible. Thus, it goes on.

So total hand shakes = N-1 + N-2 + N-3 +………+1 + 0

Input: 10

Output: 45

"""


# input number of people
people = int(input("Number of people: "))

# store handshakes in a variable
handshakes = 0

# calculating handshakes
for i in range(people - 1, 0, -1):
    handshakes += i
    
# Number of handshakes
print(handshakes)
