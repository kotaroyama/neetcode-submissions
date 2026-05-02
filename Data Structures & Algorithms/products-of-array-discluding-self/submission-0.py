class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i - 1] * nums[i - 1])

        suffix = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = 1
            else:
                suffix[i] = suffix[i + 1] * nums[i + 1]
        
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        
        return result