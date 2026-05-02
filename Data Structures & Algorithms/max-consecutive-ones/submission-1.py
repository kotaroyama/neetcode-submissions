class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_value = 0
        num_of_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                num_of_ones += 1
            if nums[i] == 0 or i == len(nums) - 1:
                # if num_of_ones > max_value:
                #     max_value = num_of_ones
                max_value = max(max_value, num_of_ones)
                num_of_ones = 0
        
        return max_value