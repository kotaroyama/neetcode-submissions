class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palidrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return is_palidrome(i + 1, j) or is_palidrome(i, j - 1)
            else:
                i += 1
                j -= 1

        return True