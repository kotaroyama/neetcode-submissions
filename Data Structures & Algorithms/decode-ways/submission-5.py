class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n == len(s):
                return 1
            if s[n] == "0":
                return 0
            
            result = dfs(n + 1)
            if n < len(s) - 1:
                if (s[n] == "1" or
                    (s[n] == "2" and s[n + 1] <= "6")):
                    result += dfs(n + 2)
            if n not in memo:
                memo[n] = result
            return memo[n]
        
        return dfs(0)