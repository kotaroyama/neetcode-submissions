class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = defaultdict(int)
        for h in hand:
            freq[h] += 1

        min_heap = list(freq.keys())
        heapq.heapify(min_heap)
        while min_heap:
            smallest_key = min_heap[0]
            for i in range(smallest_key, smallest_key + groupSize):
                if freq[i] == 0:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
  
        return True
