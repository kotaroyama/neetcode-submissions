class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = 0
        carry = 0

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            sum_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if sum_bit:
                result = result | (1 << i)
        
        mask = 0xFFFFFFFF
        if result > 0x7FFFFFFF:
            result = ~(result ^ mask)
        
        return result