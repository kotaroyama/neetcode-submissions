class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def helper(x, y):
            result = 0
            pwr = 1
            i = 1
            while i <= len(x):
                result += int(x[-i]) * int(y) * pwr
                pwr *= 10
                i += 1
            return result
        
        pwr = 1
        result = 0
        i = 1
        while i <= len(num2):
            result += helper(num1, num2[-i]) * pwr
            pwr *= 10
            i += 1
        
        return str(result)