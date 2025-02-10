def solution(n):
    res = 0
    while n > 0:
        dd = n % 100
        if dd % 11 == 0:
            res += 1
        n //= 10
    return res
    pass