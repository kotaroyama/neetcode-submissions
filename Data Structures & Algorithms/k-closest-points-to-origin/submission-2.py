class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            heap.append([distance, point])

        heapq.heapify_max(heap)
        while len(heap) > k:
            heapq.heappop_max(heap)
        
        result = []
        for item in heap:
            result.append(item[1])

        return result