class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def dfs(i, total):
            if i == len(nums):
                return total
            return max(total + nums[i], dfs(i + 1, total + nums[i]))
        
        result = min(nums)
        for i in range(len(nums)):
            result = max(result, dfs(i, 0))
        return result