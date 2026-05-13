class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify_max(heap)
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush_max(heap, (distance, point))
            if len(heap) > k:
                heapq.heappop_max(heap)
            
        result = []
        for item in heap:
            result.append(item[1])

        return result