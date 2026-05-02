class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums.extend(nums)
        return nums