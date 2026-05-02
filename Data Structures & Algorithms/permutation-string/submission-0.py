class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0
        r = len(s1) - 1
        print(r)
        s1_hash = self.hash_string(s1)
        while r < len(s2):
            if self.hash_string(s2[l:r+1]) == s1_hash:
                return True

            l += 1
            r += 1
        return False
        
    def hash_string(self, s):
        hash_table = defaultdict(int)
        for c in s:
            hash_table[c] += 1
        return hash_table