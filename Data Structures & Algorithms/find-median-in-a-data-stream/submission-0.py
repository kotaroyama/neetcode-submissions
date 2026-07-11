class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        heapq.heapify_max(self.array)
        heapq.heappush_max(self.array, num)

    def findMedian(self) -> float:
        tmp_array = self.array.copy()
        orig_len = len(self.array)
        while len(tmp_array) > orig_len / 2:
            result = heapq.heappop_max(tmp_array)

        # Even length
        if orig_len % 2 != 0:
            return result

        # Odd length
        result += heapq.heappop_max(tmp_array)
        return result / 2