class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 2
        target = len(nums) - 1
        while i >= 0:
            if i + nums[i] >= target:
                target = i
            i -= 1
        if target == 0:
            return True
        
        return False