def reversed_triple_chars(s: str) -> str:
    res = ''
    n = len(s)
    k = 0
    for i in range(2, n - (n % 3), 3):
        res += s[k:i+1][::-1]
        k = i + 1
    res += s[k:]
    return res