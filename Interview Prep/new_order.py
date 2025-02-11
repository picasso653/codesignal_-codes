def solution(numbers):
    new_order =[]
    mid = len(numbers) // 2
    if len(numbers) % 2 == 1:
        left = mid - 1
        right = mid + 1
        new_order.append(numbers[mid])
    else:
        left = mid - 1
        right = mid
    while left >= 0 and right <= len(numbers):
        p = numbers[left] * numbers[right]
        new_order.append(p)
        left -= 1
        right += 1
    return new_order
    pass