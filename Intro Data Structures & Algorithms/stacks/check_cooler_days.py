def days_until_cooler(temps):
    result = [-1] 
    stack = []
    j = 1

    for i in range(len(temps) - 1, -1, -1):
        # implement this
        while stack and stack[-1] >= temps[i]:
            stack.pop()
            j +=1
        result.append(j if stack else -1) 
        stack.append(temps[i])
    
    return result[1:][::-1]

print(days_until_cooler([30, 60, 90, 120, 60, 30]))  # Expected: [-1, 4, 2, 1, 1, -1]
print(days_until_cooler([100, 95, 90, 85, 80, 75]))  # Expected: [1, 1, 1, 1, 1, -1]
print(days_until_cooler([1]))  # Expected: [-1]