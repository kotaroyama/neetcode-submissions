class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def dfs(i, total):
            key = (i, total)
            if i == len(nums):
                return total
            if key in memo:
                return memo[key]
    
            memo[key] = max(total + nums[i], dfs(i + 1, total + nums[i]))
            return memo[key]
        
        result = min(nums)
        memo = {}
        for i in range(len(nums)):
            result = max(result, dfs(i, 0))
        return result