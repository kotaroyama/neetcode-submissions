class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = defaultdict(int)
        for n in nums:
            count_hash[n] += 1
        sorted_count_hash = dict(sorted(count_hash.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_count_hash)[:k]
