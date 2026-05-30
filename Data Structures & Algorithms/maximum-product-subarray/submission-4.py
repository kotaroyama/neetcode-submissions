class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        if N == 2:
            return max(nums[0], nums[1], nums[0] * nums[1])
        
        result = nums[0] * nums[1]
        cur_max = result
        cur_min = result
        i = 2
        while i < N:
            tmp = cur_max
            cur_max = max(nums[i], cur_max * nums[i], cur_min * nums[i])
            cur_min = min(nums[i], tmp * nums[i], cur_min * nums[i])
            result = max(result, cur_max)

            i += 1
            
        return result
