def solution(n):
    res = 0
    i = 0
    while n > 0:
        dd = (n % 10) * 11
        res += dd * (10 ** i)
        i += 2
        n //= 10
    return res
    pass