def solution(numbers):
    result = []
    n = len(numbers)
    for i in range(n // 2):
        x = numbers[i] + numbers[n - i - 1]
        result.append(x)
    if n % 2 == 1:
        result.append(numbers[(n // 2)] * 2)
    return result
    pass