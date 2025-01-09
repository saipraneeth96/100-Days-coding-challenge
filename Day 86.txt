Day 86 coding Statement : 

Mahesh got a beautiful array named A as a birthday gift from his beautiful girlfriend Namratha. There are N positive integers in that array. Mahesh loved the array so much that he started to spend a lot of time on it everyday. One day, he wrote down all possible subsets of the array. Then for each subset, he calculated the sum of elements in that subset and wrote it down on a paper. Unfortunately, Mahesh lost the beautiful array :(. He still has the paper on which he wrote all subset sums. Your task is to rebuild beautiful array A and help the couple stay happy :)

def reconstruct_array(T, test_cases):
    results = []
    for t in range(T):
        N = test_cases[t][0]
        subset_sums = sorted(test_cases[t][1])  # Sort the subset sums
        
        array = []
        used_sums = []  # To track subsets we’ve accounted for
        
        for _ in range(N):
            # The smallest positive subset sum is an element of A
            for x in subset_sums:
                if x != 0:
                    smallest = x
                    break
            
            array.append(smallest)
            
            # Generate all subsets including `smallest` and add them to new_sums
            new_sums = []
            for used in used_sums:
                new_sums.append(used + smallest)

            # Add the smallest itself (the new single element subset)
            new_sums.append(smallest)

            # Remove these sums from subset_sums
            updated_sums = []
            i, j = 0, 0
            while i < len(subset_sums) and j < len(new_sums):
                if subset_sums[i] == new_sums[j]:
                    j += 1  # Skip the sum as it is now used
                else:
                    updated_sums.append(subset_sums[i])
                i += 1

            # Add any remaining unused subset sums
            updated_sums.extend(subset_sums[i:])

            subset_sums = updated_sums
            used_sums.extend(new_sums)

        results.append(" ".join(map(str, sorted(array))))

    return results


# Input processing
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    subset_sums = list(map(int, input().split()))
    test_cases.append((N, subset_sums))

# Solve and output results
results = reconstruct_array(T, test_cases)
for result in results:
    print(result)
