def solution(numbers):
    result = []
    n = len(numbers)
    for i in numbers:
        rev = int(str(i)[::-1])
        if rev in numbers:
            result.append((i, rev))
    return result
    pass