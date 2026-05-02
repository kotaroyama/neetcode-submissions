class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        i = 0
        j = 1
        while i < len(s) and j < len(s):
            if s[i] != s[-j]:
                return False
            i += 1
            j += 1
        return True
