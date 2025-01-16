Day 93 coding Statement : 

After IOI Ilya decided to make a business. He found a social network called "TheScorpyBook.com". It currently has N registered users. As in any social network two users can be friends. Ilya wants the world to be as connected as possible, so he wants to suggest friendship to some pairs of users. He will suggest user u to have a friendship with user v if they are not friends yet and there is a user w who is friends of both of them. Note that u, v and w are different users. Ilya is too busy with IPO these days, so he asks you to count how many friendship suggestions he has to send over his social network.



def count_friendship_suggestions(n, adj):
    suggestions = 0
    
    # Iterate over all pairs of users (u, v)
    for u in range(n):
        for v in range(n):
            if u != v and adj[u][v] == '0':  # u and v are not friends
                # Check if there exists a w such that u-w and w-v are friends
                for w in range(n):
                    if w != u and w != v and adj[u][w] == '1' and adj[w][v] == '1':
                        suggestions += 1
                        break  # Only count once per (u, v)
    
    return suggestions

# Input Parsing
n = int(input())
adj = [input().strip() for _ in range(n)]

# Solve and Output Result
result = count_friendship_suggestions(n, adj)
print(result)
