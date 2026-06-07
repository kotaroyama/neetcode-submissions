class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def dfs(i, total):
            if i == len(nums):
                return total
            if (i, total) in memo:
                return memo[(i, total)]
    
            memo[(i, total)] = max(total + nums[i], dfs(i + 1, total + nums[i]))
            return memo[(i, total)]
        
        result = min(nums)
        memo = {}
        for i in range(len(nums)):
            result = max(result, dfs(i, 0))
        return result