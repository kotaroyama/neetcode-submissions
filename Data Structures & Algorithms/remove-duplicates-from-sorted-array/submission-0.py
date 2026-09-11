class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 1
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                del nums[j]
            else:
                result += 1
                i += 1
                j += 1
        return result

