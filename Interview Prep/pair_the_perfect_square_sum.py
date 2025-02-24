def solution(arr1, arr2):
    res = []
    for i in arr1:
        for j in arr2:
            if i+j >= 0 and ((i+j)**(1/2)).is_integer():
                res.append((i, j))
            else:
                continue
    return res
    pass