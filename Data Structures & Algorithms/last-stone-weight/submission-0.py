class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                new_stone = stone1 - stone2
                heapq.heappush_max(stones, new_stone)
        
        if stones:
            return stones[0]
        
        return 0