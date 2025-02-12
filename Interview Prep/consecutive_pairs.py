#The input string is always even

def solution(s):
    res = ''
    current_pair = None
    current_pair_number = 0
    current_index = 0
    for i in range(2, len(s) + 2, 2):
        k = s[current_index: i]
        if current_pair == k:
            current_pair_number += 1
        else:
            if current_pair is not None:
                res += current_pair + str(current_pair_number)
            current_pair = k
            current_pair_number = 1
        current_index = i
    if current_pair is not None:
        res += current_pair + str(current_pair_number)
    return res
    pass