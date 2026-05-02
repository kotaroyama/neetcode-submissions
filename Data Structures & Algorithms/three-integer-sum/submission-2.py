class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                if j == i:
                    j += 1
                if k == i:
                    k -= i
            
                if sorted_nums[j] + sorted_nums[k] < -sorted_nums[i]:
                    j += 1
                elif sorted_nums[j] + sorted_nums[k] > -sorted_nums[i]:
                    k -= 1
                else:
                    results.append((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                    k -= 1

        filtered_results = []
        for result in results:
            if sorted(result) not in filtered_results:
                filtered_results.append(sorted(result))
 

        return filtered_results