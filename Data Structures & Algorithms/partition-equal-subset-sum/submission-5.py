class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Get all subsets of size len(nums) / 2 of nums.
        If two of these subsets have the same sums, return True.
        Othrwise, return False
        """
        N = len(nums)
        if sum(nums) % 2 != 0:
            return False

        target_sum = int(sum(nums) / 2)
        memo = {}

        def dfs(i, cur_sum):
            if f"{i}_{cur_sum}" in memo:
                return memo[f"{i}_{cur_sum}"]

            if cur_sum == target_sum:
                return True
            if i == N:
                print(cur_sum)
                return False

            if cur_sum + nums[i] > target_sum:
                memo[f"{i}_{cur_sum}"] = dfs(i + 1, cur_sum)
            else:
                memo[f"{i}_{cur_sum}"] = dfs(i + 1, cur_sum + nums[i])
            return memo[f"{i}_{cur_sum}"]

        result = False
        for i in range(N):
            result = result or dfs(i, 0)

        return result