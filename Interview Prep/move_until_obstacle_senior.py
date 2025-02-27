def solution(numbers):
    n = len(numbers)
    result = numbers[:]

    for i in range(n):
        if numbers[i] < 0:
            result[i] = -1  # Replace obstacles with -1
        else:
            max_jump = numbers[i]
            for step in range(1, max_jump + 1):
                if i + step < n and numbers[i + step] < 0:
                    result[i] = i + step
                    break
            else:
                result[i] = numbers[i]  # Keep original value if no obstacles are found

    return result


# Example test case
print(solution([3, 2, -3, 1, 2]))  # Output: [2, 2, -1, 1, 2]
