class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            
            result = dfs(i + 1, total + nums[i])
            result += dfs(i + 1, total - nums[i])
            return result
        
        return dfs(0, 0)