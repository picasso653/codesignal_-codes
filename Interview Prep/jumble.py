def repeat_char_jump(inputString, k):
   length = len(inputString)
   result = ''
   visited = [False] * length
   i = 0
   while not all (visited):
    result += inputString[i]
    visited[i] = True
    i = (i + k) % length
   return result 