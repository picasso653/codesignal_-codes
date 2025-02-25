def solution(sentence, c):
    words = sentence.split(' ')
    result = ''
    for word in words:
        if len(word) % 2 == 0:
            mid = len(word) // 2
            for i in word[mid:]:
                if ord(i) < ord(c):
                    result += i
    return result