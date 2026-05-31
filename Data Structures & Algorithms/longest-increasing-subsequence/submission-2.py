class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n == len(nums) - 1:
                return 0
            
            result = 0
            for i in range(n + 1, len(nums)):
                if nums[i] > nums[n]:
                    result = max(result, dfs(i) + 1)
            memo[n] = result
            return memo[n]
        
        result = 0
        for i in range(len(nums)):
            result = max(result, dfs(i))
        return result + 1