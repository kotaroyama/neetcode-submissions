class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        result = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            result = (result * 10) + digit
            if result < MIN or result > MAX:
                return 0

        return result