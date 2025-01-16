"""
Day 91 coding Statement : 

Sridhar was a seasoned traveler. He liked to visit new places. More than all he was a meticulous planner. 
This time he was planning to visit Europe. He wrote down his travel itinerary like as follows:
If he wanted to visit Madrid, Paris, Munich, Warsaw and Kiev in this order, he would write it down like as:

Madrid Paris 100

Paris Munich 200

Munich Warsaw 150

Warsaw Kiev 120

More formally, if he wanted to go from A to B directly and the price is C dollars, then he would write

A B C

on a card. Each move was written on a different card. Sridhar was a great planner, so he would never visit the same place twice. Just before starting his journey, the cards got shuffled. Help Sridhar figure out the actual order of the cards and the total cost of his journey.

"""

def reconstruct_itinerary(N, trips):
    next_city = {}  # Maps a city to (next_city, cost)
    in_degree = {}  # Tracks cities that are destinations
        
    for A, B, C in trips:
        C = int(C)
        next_city[A] = (B, C)
        in_degree[B] = in_degree.get(B, 0) + 1
        if A not in in_degree:
            in_degree[A] = 0
        
    # Find the starting city
    start = None
    for city in in_degree:
        if in_degree[city] == 0:  # City with no incoming trips
            start = city
            break
        
    # Reconstruct the sequence
    ordered_itinerary = []
    total_cost = 0
    current = start
        
    while current in next_city:
        next_stop, cost = next_city[current]
        ordered_itinerary.append(f"{current} {next_stop} {cost}")
        total_cost += cost
        current = next_stop

    return ordered_itinerary + [str(total_cost)]


# Input number of test cases
T = int(input())

for i in range(T):
    N = int(input())
    trips = [input().split() for _ in range(N - 1)]
    
    result = reconstruct_itinerary(N, trips)
    
    # display the result
    print("\n".join(result))
