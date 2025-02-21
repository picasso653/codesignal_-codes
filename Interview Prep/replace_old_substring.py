def replace_substring(text, old, new):
    n = 0
    k = len(old)
    res = ''
    while n <= len(text) - k:
        idx = text.find(old, n)
        if idx == -1:
            # res += text[n:]
            break
        else:
            res += text[n:idx]
            res += new
        n = idx + k
    res += text[n:]
    return res if res != '' else text

    pass

text = "hello world, hello universe"
old = "hello"
new = "hi"
result = replace_substring(text, old, new)
print(result)