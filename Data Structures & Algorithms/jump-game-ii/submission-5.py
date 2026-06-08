class Solution:
    def jump(self, nums: List[int]) -> int:

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]

            result = 1001
            for j in range(i + 1, i + nums[i] + 1):
                result = min(result, 1 + dfs(j))
            memo[i] = result
            return memo[i]
        
        memo = {}
        return dfs(0)