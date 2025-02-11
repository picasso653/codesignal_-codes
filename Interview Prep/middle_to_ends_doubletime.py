def unusual_traversal(array):
    mid = len(array) // 2
    left = mid - 1
    right = mid + 1
    new_order = [array[mid]]

    while left >= 0 or right < len(array):
        if left >= 1:
            new_order.append(array[left - 1])
            new_order.append(array[left])
            left -= 2
        elif left == 0:
            new_order.append(array[left])
            left -= 1
        if right < len(array) - 1:
            new_order.append(array[right])
            new_order.append(array[right + 1])
            right += 2
        elif right == len(array) - 1:
            new_order.append(array[right])
            right += 1

    return new_order