class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        flag = False
        hash_map = {}

        for i in range(len(matrix)):
            flag = False
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    flag = True
                    hash_map[j] = True
            if flag:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
            
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j in hash_map:
                    matrix[i][j] = 0