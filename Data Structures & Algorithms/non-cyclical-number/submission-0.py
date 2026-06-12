class Solution:
    def isHappy(self, n: int) -> bool:

        def get_digits(num) -> list[int]:
            digits = []
            while num > 0:
                digits.append(num % 10)
                num = int(num / 10)
            return digits
        
        def get_square_sum(digits) -> int:
            total = 0
            for digit in digits:
                total += digit ** 2
            return total

        hash_map = {}
        digits = get_digits(n)
        
        while True:
            square_sum = get_square_sum(digits)
            if square_sum in hash_map:
                return False
            if square_sum == 1:
                return True
            hash_map[square_sum] = 1
            digits = get_digits(square_sum)
            