import heapq

heap = []

# Insert in heap
heapq.heappush(heap, 4)
heapq.heappush(heap, 9)
heapq.heappush(heap, 6)

print("Heap after insertion: ", heap)
# Output: Heap after insertion:  [4, 9, 6]

# Delete the smallest element from the heap
heapq.heappop(heap)
print("Heap after deletion: ", heap)
# Output: Heap after deletion:  [6, 9]

# Extract the smallest element
smallest = heapq.nsmallest(1, heap)[0]
print("Smallest element in the heap: ", smallest)
# Output: Smallest element in the heap:  6