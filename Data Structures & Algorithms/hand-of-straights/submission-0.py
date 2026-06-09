class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = defaultdict(int)
        for h in hand:
            freq[h] += 1

        while freq:
            smallest_key = min(freq)
            for i in range(smallest_key, smallest_key + groupSize):
                if freq.get(i, 0) == 0:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    del freq[i]
  
        return True


            
