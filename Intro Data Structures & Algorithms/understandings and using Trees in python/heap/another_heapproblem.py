import heapq

class MiddleElementFinder:
    def __init__(self):
        self.heaps = [], []

    def add_num(self, num: int) -> None:
        # implement this
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))
        pass

    def middle_element(self) -> float:
        # implement this
        small, large = self.heaps
        return float((large[0] + -small[0]) / 2) if len(small) > len(large) else float(large[0])

# Let's test the code
estimate_finder = MiddleElementFinder()
estimate_finder.add_num(5)
estimate_finder.add_num(10)
estimate_finder.add_num(3)
estimate_finder.add_num(1)
estimate_finder.add_num(7)

print(estimate_finder.middle_element()) # Expected output: 5