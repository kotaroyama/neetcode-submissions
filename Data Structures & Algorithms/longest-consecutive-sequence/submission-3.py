class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_table = defaultdict(bool)

        for num in nums:
            hash_table[num] = True
        
        min_value = min(nums)
        max_value = max(nums)
        local_len = 0
        max_len = 0
        for i in range(min_value, max_value + 2):
            if hash_table[i - 1]:
                local_len += 1
                max_len = max(max_len, local_len)
            else:
                local_len = 0
        return max_len