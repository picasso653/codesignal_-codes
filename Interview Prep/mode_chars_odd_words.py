def solution(sentence):
    words = sentence.split(' ')
    result = ''
    for word in words:
        if len(word) % 2 == 1:
            counter = ("", 0)
            for i in word.lower():

                if word.lower().count(i) > counter[1]:
                    counter = (i, word.lower().count(i))
            result += counter[0]
    return result