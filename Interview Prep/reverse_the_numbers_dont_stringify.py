def solution(n):
    res = 0
    while n > 0:
        digit = n % 10
        res *= 10
        res += digit
        n = n // 10
    return res
    pass