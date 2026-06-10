class Solution:
    def checkValidString(self, s: str) -> bool:
        
        def dfs(i, open_p):
            if i == len(s):
                if open_p == 0:
                    return True
                return False
            if open_p < 0:
                return False
            
            key = (i, open_p)
            if key in memo:
                return memo[key]
            
            if s[i] == "(":
                result = dfs(i + 1, open_p + 1)
            elif s[i] == ")":
                result = dfs(i + 1, open_p - 1)
            else:
                result = (dfs(i + 1, open_p + 1) or
                        dfs(i + 1, open_p - 1) or
                        dfs(i + 1, open_p))
            memo[key] = result
            return memo[key]
        
        memo = {}
        return dfs(0, 0)