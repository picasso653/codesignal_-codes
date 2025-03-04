def solution(num1, num2):
    # Compare lengths first
    if len(num1) > len(num2):
        return 1
    elif len(num1) < len(num2):
        return -1

    # If lengths are the same, compare digit by digit
    for i in range(len(num1)):
        if num1[i] > num2[i]:
            return 1
        elif num1[i] < num2[i]:
            return -1

    # If no differences are found, the numbers are equal
    return 0


# Test cases
print(solution('12345', '1234'))  # Output: 1
print(solution('1234', '12345'))  # Output: -1
print(solution('12345', '12345'))  # Output: 0
