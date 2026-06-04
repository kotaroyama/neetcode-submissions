class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def dfs(index1, index2, index3):
            key = (index1, index2)
            if index3 == len(s3):
                if index1 == len(s1) and index2 == len(s2):
                    return True
                else:
                    return False
            if key in memo:
                return memo[key]
            
            result = False
            if ((index1 < len(s1) and index2 < len(s2)) and
                s3[index3] == s1[index1] and
                s3[index3] == s2[index2]):
                result = result or dfs(index1 + 1, index2, index3 + 1)
                result = result or dfs(index1, index2 + 1, index3 + 1)
            elif index1 < len(s1) and s3[index3] == s1[index1]:
                result = result or dfs(index1 + 1, index2, index3 + 1)
            elif index2 < len(s2) and s3[index3] == s2[index2]:
                result = result or dfs(index1, index2 + 1, index3 + 1)
            memo[key] = result
            return result            

        memo = {}
        return dfs(0, 0, 0)