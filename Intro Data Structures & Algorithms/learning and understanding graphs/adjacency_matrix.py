users = 4  # 4 users: A: 0, B: 1, C: 2, D: 3
M = [[0] * users for _ in range(users)]

# Add friendships, A-B and B-C
M[0][1] = M[1][0] = 1
M[1][2] = M[2][1] = 1

# Print the adjacency matrix
for row in M:
    print(row)

# Output:
# [0, 1, 0, 0]
# [1, 0, 1, 0]
# [0, 1, 0, 0]
# [0, 0, 0, 0]

# Check for friend suggestions
for i in range(users):
    for j in range(i + 1, users):
        if i != j and M[i][j] == 0 and any((M[i][k] == 1 and M[k][j] == 1) for k in range(users)):
            print(f"User {i} and User {j} may know each other.")

# Output:
# User 0 and User 2 may know each other.