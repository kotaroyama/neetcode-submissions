class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(len(strs[0])):
            for s in strs:
                if not s or i == len(s) or strs[0][i] != s[i]:
                    return result
            
            result += strs[0][i]
        
        return result