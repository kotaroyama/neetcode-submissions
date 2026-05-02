# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        mid = (low + high) // 2

        while low <= high:
            guess_num = guess(mid)
            if guess_num == -1:
                high = mid - 1
            elif guess_num == 1:
                low = mid + 1
            else:
                return mid
            mid = (low + high) // 2