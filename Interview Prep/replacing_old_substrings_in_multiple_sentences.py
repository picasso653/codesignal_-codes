def solution(sentences, words):
    res = []

    for sentence, word in zip(sentences, words):
        k = 0
        new = ''
        n = len(word)

        while True:
            idx = sentence.lower().find(word.lower(), k)  # Case-insensitive search
            if idx == -1:
                break  # No more occurrences

            new += sentence[k:idx]  # Add text before the found word
            found_word = sentence[idx:idx + n]  # Reverse word while preserving case
            reversed_word = found_word[::-1]
            if found_word[0].isupper():
                reversed_word = reversed_word.capitalize()
            new += reversed_word
            k = idx + n  # Move search forward

        new += sentence[k:]  # Add remaining part of sentence
        res.append(new)

    return res
