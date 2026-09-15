class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i in range(len(nums)):
            hash_table[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_table and hash_table[diff] != i:
                return [i, hash_table[diff]]
