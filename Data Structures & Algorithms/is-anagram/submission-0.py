class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = self.char_hash(s)
        hash_t = self.char_hash(t)

        if hash_s == hash_t:
            return True
        
        return False
        
    
    def char_hash(self, text: str):
        char_hash = {}
        for char in text:
            if char not in char_hash:
                char_hash[char] = 1
            else:
                char_hash[char] += 1
        return char_hash