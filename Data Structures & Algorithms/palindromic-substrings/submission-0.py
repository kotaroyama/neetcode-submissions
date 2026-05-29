class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # Odd palidromes
            l = i
            r = i
            while (l >= 0 and r < len(s) and
                s[l] == s[r]):
                l -= 1
                r += 1
                count += 1
            
            # Even palidoromes
            l = i
            r = i + 1
            while (l >= 0 and r < len(s) and
                s[l] == s[r]):
                l -= 1
                r += 1
                count += 1

        return count
            
