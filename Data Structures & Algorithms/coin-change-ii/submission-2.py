class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(i, total):
            key = (i, total)
            if total == 0:
                return 1
            if total < 0:
                return 0
            if key in memo:
                return memo[key]
            
            result = 0
            for j in range(i, len(coins)):
                result += dfs(j, total - coins[j])
            memo[key] = result
            return memo[key]
        memo = {}
        return dfs(0, amount)