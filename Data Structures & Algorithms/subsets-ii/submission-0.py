class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curset = []
        nums.sort()
        self.helper(0, nums, subsets, curset)

        return subsets

    def helper(self, i, nums, subsets, curset):
        if i == len(nums):
            if curset.copy() not in subsets:
                subsets.append(curset.copy())
            return

        curset.append(nums[i])
        self.helper(i + 1, nums, subsets, curset)

        curset.pop()
        self.helper(i + 1, nums, subsets, curset)