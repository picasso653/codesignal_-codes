def evaluatePath(numbers):
    n = len(numbers)
    position = 0  # Start at the first position
    moves = 0  # Counter for moves
    direction = 1  # 1 for right, -1 for left
    reversed_once = False  # To track if direction has been reversed

    while True:
        step = numbers[position] * direction  # Determine actual movement

        if step == 0:
            break  # Blockade encountered, game ends

        new_position = position + step

        if new_position < 0 or new_position >= n:
            if reversed_once:
                break  # If already reversed, game ends
            direction *= -1  # Reverse the direction
            reversed_once = True
        else:
            position = new_position  # Move to the new position
            moves += 1

    return (position, moves)
