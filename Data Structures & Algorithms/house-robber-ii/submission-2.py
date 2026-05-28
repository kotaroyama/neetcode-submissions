class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(n, flag, memo):
            if n in memo:
                return memo[n]
            if n >= len(nums) or (n == len(nums) - 1 and flag):
                return 0
            
            if n not in memo:
                memo[n] = max(dfs(n + 1, flag, memo), nums[n] + dfs(n + 2, flag, memo))
            return memo[n]
        
        result = max(dfs(0, True, {}), dfs(1, False, {}))
        return result