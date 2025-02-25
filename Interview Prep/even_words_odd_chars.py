def solution(sentence):
    words = sentence.split(' ')
    result = ''
    for word in words:
        if len(word) % 2 == 0:  # check if the length of word is even
            for i in range(1, len(word), 2):  # loop over odd characters
                result += word[i]
    return result