class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 0
        cur_sum = 0
        i = 0
        for j in range(0, len(nums)):
            cur_sum += nums[j]
            if cur_sum >= target:
                if result == 0:
                    result = j - i + 1
                while (cur_sum - nums[i]) >= target:
                    cur_sum -= nums[i]
                    i += 1
                    result = min(result, j - i + 1)
        return result
