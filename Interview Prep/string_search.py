def stringSearch(sourceArray, searchArray):
    res = []
    for tp in sourceArray:
        for sl in searchArray:
            if tp[0] <= sl[0] and tp[1] in sl[1]:
                res.append(tp)
                break
    return res
    pass