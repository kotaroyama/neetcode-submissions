class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        count = 0
        
        def dfs(r, c):
            if (min(r, c) < 0 or
                r == ROWS or
                c == COLS or 
                (r, c) in visited):
                return
            
            if grid[r][c] == "0":
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    dfs(i, j)

        return count