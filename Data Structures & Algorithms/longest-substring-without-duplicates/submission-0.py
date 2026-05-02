class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        l = 0
        r = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            max_len = max(max_len, r - l + 1)
        
        return max_len
