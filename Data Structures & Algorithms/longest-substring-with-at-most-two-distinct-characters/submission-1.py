class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
            
        char_hash = defaultdict(int)
        result = 0
        i = 0
        j = 1

        char_hash[s[0]] += 1
        char_hash[s[1]] += 1
        j += 1
        
        while j < len(s):
            char_hash[s[j]] += 1
            char_count = len(char_hash)
            if char_count <= 2:
                j += 1
            else:
                while len(char_hash) > 2:
                    if s[i] not in s[i + 1:j + 1]:
                        del char_hash[s[i]]
                    i += 1
            result = max(result, j - i)
        
        return result
                
