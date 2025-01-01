from collections import defaultdict


def keyword_index(docs):
    # implement this
    quick_search = {}

    for idx, doc in enumerate(docs):
        for word in doc.split():
            if word in quick_search:
                quick_search[word][idx] = (doc.split()).count(word)
            else:
                quick_search[word] = {idx : (doc.split()).count(word)}
        
    return quick_search
    pass

docs = ["Hello world", "world of python", "python is a snake"]
print(keyword_index(docs))