Day 71 coding Statement:
There are N students in a class, where the i-th student has a score of Ai.

def count_boasting_students(T, test_cases):
    results = []
    for case in test_cases:
        N, scores = case
        scores.sort()  # Sort the scores
        boasting_count = 0
        
        for i in range(N):
            # Count students with scores ≤ scores[i]
            count_le = i + 1  # All elements up to the current index are ≤ scores[i]
            count_gt = N - count_le  # Remaining elements are > scores[i]
            
            if count_le > count_gt:
                boasting_count += 1
        
        results.append(boasting_count)
    return results

# Input Reading
T = int(input())  # Number of test cases
test_cases = []

for _ in range(T):
    N = int(input())  # Number of students
    scores = list(map(int, input().split()))
    test_cases.append((N, scores))

# Solve and Output
results = count_boasting_students(T, test_cases)
for res in results:
    print(res)
