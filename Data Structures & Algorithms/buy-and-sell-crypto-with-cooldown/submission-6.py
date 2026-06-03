class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def memoization(i, buying):
            key = f"{i}-{buying}"
            if i >= len(prices):
                return 0
            if key in memo:
                return memo[key]
            
            if not buying:
                memo[key] = max(memoization(i + 1, False),
                    memoization(i + 2, True) + prices[i])
            else:
                memo[key] = max(memoization(i + 1, True), 
                    memoization(i + 1, False) - prices[i])
            return memo[key]
        
        memo = {}
        return memoization(0, True)