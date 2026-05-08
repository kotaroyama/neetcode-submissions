class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_table = set()

        for num in nums:
            if num in hash_table:
                return num
            hash_table.add(num)
        
        return -1
