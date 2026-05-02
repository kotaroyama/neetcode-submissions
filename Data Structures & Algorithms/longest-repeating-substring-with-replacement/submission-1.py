class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        char_set = set(s)

        for c in char_set:
            r = 0
            l = 0
            count = 0
            while r < len(s):
                if s[r] == c:
                    count += 1
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                result = max(result, r - l + 1)
                r += 1
        return result
            
        