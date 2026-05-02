class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            count = 0
            j = i
            while j > 0:
                if j & 1 == 1:
                    count += 1
                j >>= 1
            result.append(count)
        return result
