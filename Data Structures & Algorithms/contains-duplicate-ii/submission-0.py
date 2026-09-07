class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if i + k > len(nums) - 1:
                stop = len(nums)
            else:
                stop = i + k + 1
            for j in range(i + 1, stop):
                if nums[i] == nums[j]:
                    return True
        return False