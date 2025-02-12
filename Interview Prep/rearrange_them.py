def special_order(inputString):
    a = ''
    o = ''
    n = len(inputString)
    for i in range(n // 2 + n % 2):
        o += inputString[n - 1 - i]

        if n - 1 - i != i:
            a += inputString[i]
    return o + a
    pass

print(special_order('abcdef'))