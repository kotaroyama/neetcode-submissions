class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L < R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid

        def binary_search(left, right) -> int:
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    return mid
            return -1

        pivot = L
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        result = binary_search(pivot, len(nums) - 1)
        return result