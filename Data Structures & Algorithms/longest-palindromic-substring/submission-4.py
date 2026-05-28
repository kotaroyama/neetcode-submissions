class Solution:
    def longestPalindrome(self, s: str) -> str:
        substrings = []
        for i in range(len(s)):
            substring = s[i]
            j = 1
            while i + j < len(s) and s[i] == s[i + j]:
                substring = substring + s[i + j]
                j += 1
            k = 1
            if j == 1 and len(substring) == 1:
                j = 0
            else:
                j -= 1
            while (i - k >= 0 and i + j + k < len(s) and
                s[i - k] == s[i + j + k]):
                substring = s[i - k] + substring + s[i + j + k]
                k += 1
            substrings.append(substring)
        
        max_substring = substrings[0]
        for substring in substrings:
            if len(substring) > len(max_substring):
                max_substring = substring 
        return max_substring