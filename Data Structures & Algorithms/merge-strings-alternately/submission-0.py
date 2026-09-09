class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        result = ""
        for i in range(min(len1, len2)):
            result += word1[i]
            result += word2[i]
        
        if len1 > len2:
            result += word1[len2:]
        else:
            result += word2[len1:]

        return result
