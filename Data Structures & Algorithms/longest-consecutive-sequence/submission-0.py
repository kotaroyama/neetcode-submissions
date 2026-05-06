class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_table = defaultdict(bool)

        for num in nums:
            hash_table[num] = True
        
        local_length = 0
        max_length = 0
        for key in hash_table:
            local_length = 0
            local_key = key
            while local_key in hash_table:
                local_length += 1
                local_key += 1
            max_length = max(max_length, local_length)
        
        return max_length
