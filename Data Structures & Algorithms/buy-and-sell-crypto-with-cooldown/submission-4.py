class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def memoization(i, having, prev_date, cache):
            key = f"{having}-{prev_date}"
            if i == len(prices):
                return 0
            if key in cache:
                return cache[key]
            
            if having:
                profit = prices[i] - prices[prev_date]
                cache[key] = max(profit + memoization(i + 1, False, i, cache),
                               memoization(i + 1, having, prev_date, cache))
            else:
                if prev_date == i - 1 and prev_date != -1:
                    cache[key] = memoization(i + 1, having, prev_date, cache)
                else:
                    cache[key] = max(memoization(i + 1, True, i, cache),
                                   memoization(i + 1, having, prev_date, cache))
            return cache[key]
        
        memo = {}
        return memoization(0, False, -1, memo)