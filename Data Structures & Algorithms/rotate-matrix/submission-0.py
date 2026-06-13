class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        for i in range(int(n / 2)):
            tmp = matrix[i].copy()
            matrix[i] = matrix[-(i + 1)].copy()
            matrix[-(i + 1)] = tmp
        
        for i in range(n):
            for j in range(i + 1, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp