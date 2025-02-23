def spot_swaps(source: str, target: str) -> list:
    res = []
    for i in range(len(source) - 1):
        if source[i] != target[i] and source[i+1] == target[i] and source[i] == target[i+1]:
            res.append((i,source[i], source[i+1]))
    return res
    pass