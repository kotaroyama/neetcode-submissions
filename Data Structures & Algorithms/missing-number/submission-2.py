class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_set = {}
        for i, num in enumerate(nums):
            hash_set[num] = i
        
        for i in range(len(nums) + 1):
            if i not in hash_set:
                return i
            