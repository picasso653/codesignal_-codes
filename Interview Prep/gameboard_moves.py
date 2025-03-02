def solution(board, obstacle):
    n = len(board)
    moves = [-1] * n  # Initialize all moves to -1

    for i in range(n):
        if board[i] == obstacle:
            continue  # Skip positions that are obstacles

        steps = 0
        position = i

        while position < n:
            if board[position] == obstacle:
                steps = -1
                break

            next_position = position + board[position]
            steps += 1

            if next_position >= n:
                break  # Exit the board

            position = next_position

        moves[i] = steps

    return moves

# Example usage
print(solution([5, 3, 2, 6, 2, 1, 7], 3))  # Output: [3, -1, 3, 1, 2, 2, 1]
