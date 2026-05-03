class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] == target:
                return True
            elif row[-1] > target:
                L = 0
                R = len(row) - 1
                mid = (L + R) // 2
                while L <= R:
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        R = mid - 1
                    else:
                        L = mid + 1
                    mid = (L + R) // 2
                return False
        return False