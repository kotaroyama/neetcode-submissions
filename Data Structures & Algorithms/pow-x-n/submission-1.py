class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return float(1)
        result = x
        i = 1
        if n >= 0:
            while i < n:
                result = result * x
                i += 1
            return result
        else:
            m = abs(n)
            while i < m:
                result = result * x
                i += 1
            return 1/result