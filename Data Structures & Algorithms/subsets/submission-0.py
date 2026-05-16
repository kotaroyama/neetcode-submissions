class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curset = []
        self.helper(0, nums, subsets, curset)
        return subsets

    def helper(self, i, nums, subsets, curset):
        if i >= len(nums):
            subsets.append(curset.copy())
            return
        
        curset.append(nums[i])
        self.helper(i + 1, nums, subsets, curset)
        curset.pop()
        self.helper(i + 1, nums, subsets, curset)