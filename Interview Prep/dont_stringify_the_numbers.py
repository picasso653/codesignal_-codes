def solution(n):
    res = 1
    odd = False
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            odd = True
            res *= digit
        n = n // 10
    return res if odd else 0
    pass