class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = defaultdict(int)
        for n in nums:
            count_hash[n] += 1
        count_array = [[] for _ in range(len(nums) + 1)]
        for key, value in count_hash.items():
            count_array[value].append(key)
        result = []
        count = 0
        for i in range(len(count_array) - 1, 0, -1):
            if count_array[i]:
                result.extend(count_array[i])
            if len(result) >= k:
                break
        return result