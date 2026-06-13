class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []

        upper = 0
        lower = len(matrix) 
        left = 0
        right = len(matrix[0])

        while upper < lower and left < right:
            for i in range(left, right):
                order.append(matrix[upper][i])
            upper += 1

            for i in range(upper, lower):
                order.append(matrix[i][right - 1])
            right -= 1

            if not (upper < lower and left < right):
                break

            for i in range(right - 1, left - 1, -1):
                order.append(matrix[lower - 1][i])
            lower -= 1

            for i in range(lower - 1, upper - 1, -1):
                order.append(matrix[i][left])
            left += 1

        return order