class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        hashmap_count = {}
        for num in nums:
            hashmap[num] = target - num
            if num not in hashmap_count:
                hashmap_count[num] = 1
            else:
                hashmap_count[num] += 1

        result = []
        for item in hashmap_count:
            if hashmap_count[item] > 1 and item * hashmap_count[item] == target:
                i = 0
                for num in nums:
                    if num == item:
                        result.append(i)
                    i += 1
        i = 0
        for num in nums:
            if hashmap[num] in hashmap and num != hashmap[num]:
                result.append(i)
            i += 1
        
        return result