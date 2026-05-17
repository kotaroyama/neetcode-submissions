class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hash_set = set() # (row, col)
        
        def dfs(row, col, i):
            nonlocal hash_set
            if row < 0 or col < 0 or row == len(board) or col == len(board[row]):
                return False
            if i == len(word) - 1 and board[row][col] == word[i]:
                return True
            if board[row][col] != word[i]:
                return False

            result = False
            hash_set.add((row, col))
            if (row + 1, col) not in hash_set:
                result = result or dfs(row + 1, col, i + 1)
            if (row, col + 1) not in hash_set:
                result = result or dfs(row, col + 1, i + 1)
            if (row - 1, col) not in hash_set:
                result = result or dfs(row - 1, col, i + 1)
            if (row, col - 1) not in hash_set:
                result = result or dfs(row, col - 1, i + 1)
            hash_set.discard((row, col))
            return result

        result = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                result = result or dfs(i, j, 0)
                if result:
                    return True
        
        return result

        