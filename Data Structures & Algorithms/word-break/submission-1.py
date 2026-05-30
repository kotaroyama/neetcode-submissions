class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            if i > len(s):
                return False
            
            result = False
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    result = result or dfs(j)
            memo[i] = result
            return memo[i]

        return dfs(0)
