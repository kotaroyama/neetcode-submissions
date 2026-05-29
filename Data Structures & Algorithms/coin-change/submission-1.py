class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        memo = {}
        def dfs(total):
            if total == 0:
                return 0
            if total in memo:
                return memo[total]

            result = float("inf")
            for coin in coins:
                if total - coin >= 0:
                    result = min(result, dfs(total - coin) + 1)
            memo[total] = result
            return result
    
        min_coins = dfs(amount)
        if min_coins == float("inf"):
            return -1
        return min_coins