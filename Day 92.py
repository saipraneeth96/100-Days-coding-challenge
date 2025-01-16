Day 92 coding Statement : 

Let X be the set of all integers between 0 and n-1. Suppose we have a collection S1, S2, ..., Sm of subsets of X. Say an atom A is a subset of X such that for each Si we have either A is a subset of Si or A and Si do not have any common elements.

Your task is to find a collection A1, ..., Ak of atoms such that every item in X is in some Ai and no two Ai, Aj with i ≠ j share a common item. Surely such a collection exists as we could create a single set {x} for each x in X. A more interesting question is to minimize k, the number of atoms.



def find_minimum_atoms(n, m, subsets):

    masks = set()
        
    # For each element in X, calculate its membership mask
    for x in range(n):
        mask = 0
        for i in range(m):
            if x in subsets[i]:
                mask |= (1 << i)  # Set the ith bit if x is in S_i
        masks.add(mask)
    
    return len(masks)

# Input Parsing
T = int(input())


for i in range(T):
    n, m = map(int, input().split())
    subsets = []
    for j in range(m):
        line = list(map(int, input().split()))
        subsets.append(set(line[1:]))

# Solve and Output Results
results = find_minimum_atoms(n, m, subsets)
print(results)
