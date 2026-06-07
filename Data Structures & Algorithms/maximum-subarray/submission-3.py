class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_max = 0

        for num in nums:
            if cur_max < 0:
                cur_max = 0
            cur_max += num
            
            max_sub = max(max_sub, cur_max)
        
        return max_sub