class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(n):
            if n in memo:
                return memo[n]
            if n >= len(nums) - 1:
                if n == len(nums) - 1:
                    return nums[-1]
                else:
                    return 0
            
            if n not in memo:
                memo[n] = max(nums[n] + dfs(n + 2), dfs(n + 1))
            return memo[n]
        
        return dfs(0)
