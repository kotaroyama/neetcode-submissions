class Solution:
    def firstUniqChar(self, s: str) -> int:
        character_counts = defaultdict(int)
        for c in s:
            character_counts[c] += 1
        for i in range(len(s)):
            if character_counts[s[i]] == 1:
                return i
        
        return -1