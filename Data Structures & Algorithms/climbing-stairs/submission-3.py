class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i, cache):
            if i >= n:
                if i == n:
                    return 1
                else:
                    return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1, cache) + dfs(i + 2, cache)
            return cache[i]

        cache = []
        for i in range(n):
            cache.append(-1)
        return dfs(0, cache)        




