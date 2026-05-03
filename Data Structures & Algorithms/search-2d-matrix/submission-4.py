class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L1 = 0
        R1 = len(matrix) - 1
        mid1 = (L1 + R1) // 2
        while L1 <= R1:
            if matrix[mid1][0] <= target <= matrix[mid1][-1]:
                L2 = 0
                R2 = len(matrix[mid1]) - 1
                mid2 = (L2 + R2) // 2
                while L2 <= R2:
                    if matrix[mid1][mid2] == target:
                        return True
                    elif matrix[mid1][mid2] > target:
                        R2 = mid2 - 1
                    else:
                        L2 = mid2 + 1
                    mid2 = (L2 + R2) // 2
                return False
            elif matrix[mid1][-1] > target:
                R1 = mid1 - 1
            else:
                L1 = mid1 + 1
            mid1 = (L1 + R1) // 2
        return False