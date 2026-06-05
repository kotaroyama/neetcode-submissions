class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] + 1 <= 9:
            digits[-1] = digits[-1] + 1
            return digits
        
        number = 0
        j = 10
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                number += digits[i]
            else:
                number += j * digits[i]
                j = j * 10
        number += 1
        result = []
        for c in str(number):
            result.append(int(c))
        return result