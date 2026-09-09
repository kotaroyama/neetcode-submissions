class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums) / 2
        digit_counts = defaultdict(int)
        
        for num in nums:
            digit_counts[num] += 1
            if digit_counts[num] > half:
                return num