class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        result = []
        for i in range(len(nums)):
            j = target - nums[i]
            if (j) in hashmap:
                result.append(hashmap[j])
                result.append(i)
                break
            else:
                hashmap[nums[i]] = i

        return result