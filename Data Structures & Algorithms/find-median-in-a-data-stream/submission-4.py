class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []


    def addNum(self, num: int) -> None:
        # Small: max_heap, large: min_heap
        heapq.heappush_max(self.small, num)

        # All values in small <= values in large
        if self.small and self.large and self.small[0] > self.large[0]:
            # val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, heapq.heappop_max(self.small))
        
        # Lists must be of equal size (+-1)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, heapq.heappop_max(self.small))
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush_max(self.small, heapq.heappop(self.large))

    def findMedian(self) -> float:
        print(self.small)
        print(self.large)
        print("\n\n")

        if not self.large:
            return self.small[0]
        
        if len(self.small) == len(self.large):
            return (self.small[0] + self.large[0]) / 2
        
        if len(self.small) > len(self.large):
            return self.small[0]
        else:
            return self.large[0]
