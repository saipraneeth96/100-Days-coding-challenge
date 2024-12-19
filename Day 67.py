Day 67 coding Statement: Bricks Breaking

SOLUTION:

def min_hits(S, W1, W2, W3):
    # Try the original order [W1, W2, W3]
    hits_normal = 0
    if W1 + W2 + W3 <= S:
        hits_normal = 1
    elif W1 + W2 <= S or W2 + W3 <= S:
        hits_normal = 2
    else:
        hits_normal = 3

    # Try the reversed order [W3, W2, W1]
    hits_reversed = 0
    if W3 + W2 + W1 <= S:
        hits_reversed = 1
    elif W3 + W2 <= S or W2 + W1 <= S:
        hits_reversed = 2
    else:
        hits_reversed = 3

    # Return the minimum of the two hit counts
    return min(hits_normal, hits_reversed)

# Reading input and processing each test case
T = int(input())  # number of test cases
for _ in range(T):
    S, W1, W2, W3 = map(int, input().split())
    print(min_hits(S, W1, W2, W3))
