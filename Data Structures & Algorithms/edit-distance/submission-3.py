class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        
        def dfs(index1, index2):
            key = (index1, index2)
            if index1 == len(word1):
                return len(word2) - index2
            if index2 == len(word2):
                return len(word1) - index1
            if key in memo:
                return memo[key]
            
            
            if word1[index1] == word2[index2]:
                result = dfs(index1 + 1, index2 + 1)
            else:
                result = min(1 + dfs(index1 + 1, index2),
                           1 + dfs(index1, index2 + 1),
                           1 + dfs(index1 + 1, index2 + 1))
            memo[key] = result
            return memo[key]

        memo = {}
        return dfs(0, 0)