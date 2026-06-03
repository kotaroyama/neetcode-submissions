class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            key = (i, total)
            if key in memo:
                return memo[key]
            
            result = dfs(i + 1, total + nums[i])
            result += dfs(i + 1, total - nums[i])
            memo[key] = result
            return memo[key]
        memo = {}
        return dfs(0, 0)