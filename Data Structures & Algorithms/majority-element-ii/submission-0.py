class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        req_size = len(nums) / 3
        counts = defaultdict(int)
        result = set()
        
        for num in nums:
            counts[num] += 1
            if counts[num] > req_size:
                result.add(num)

        return list(result)