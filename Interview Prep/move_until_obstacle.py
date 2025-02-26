def solution(numbers, obstacle):
    position = 0
    moves = 0
    while position < len(numbers):
        if numbers[position] == obstacle:
            return position
        moves += 1
        position += numbers[position]
    return moves