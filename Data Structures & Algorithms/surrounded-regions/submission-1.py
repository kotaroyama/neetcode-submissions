class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        def dfs(r, c):
            if (min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                (r, c) in visited or
                board[r][c] == "X"):
                return
            
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS -1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"

