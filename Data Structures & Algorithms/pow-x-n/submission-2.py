class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            result = helper(x, n // 2)
            result *= result
            if n % 2 == 1:
                result *= x
            return result

        result = helper(x, abs(n))

        if n < 0:
            return 1 / result
        return result