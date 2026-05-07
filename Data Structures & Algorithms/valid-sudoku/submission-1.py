class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for row in board:
            hash_table = defaultdict(bool)
            for item in row:
                if hash_table[item]:
                    return False
                if item != ".":
                    hash_table[item] = True

        # Check columns
        for col in range(len(board[0])):
            hash_table = defaultdict(bool)
            for row in range(len(board)):
                if hash_table[board[row][col]]:
                    return False 
                if board[row][col] != ".":
                    hash_table[board[row][col]] = True

        for i in range(3):
            for j in range(3):  
                result = [row[j * 3:j * 3 + 3] for row in board[i * 3: i * 3 + 3]]
                hash_table = defaultdict(bool) # Reset hash table
                for k in result:
                    for l in k:
                        if l in hash_table:
                            return False
                        if l != ".":
                            hash_table[l] = True

        return True

        

        
        