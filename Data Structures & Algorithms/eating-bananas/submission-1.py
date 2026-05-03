class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        speed = R
       
        while L <= R:
            mid = (L + R) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/mid)
            if hours <= h:
                speed = min(speed, mid)
                R = mid - 1
            else:
                L = mid + 1
        return speed

        