class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def memoization(r, c, rows, cols, cache):
            key = f"{r}-{c}"
            if r == rows or c == cols:
                return 0
            if key in cache:
                return cache[key]
            if r == rows - 1 and c == cols - 1:
                return 1
            
            memo[key] =(memoization(r + 1, c, rows, cols, cache) +
                        memoization(r, c + 1, rows, cols, cache))
            return memo[key]
        
        memo = {}
        return memoization(0, 0, m, n, memo)