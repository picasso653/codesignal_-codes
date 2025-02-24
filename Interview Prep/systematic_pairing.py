def solution(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            if i < j:
                result.append((i, j))
    return result