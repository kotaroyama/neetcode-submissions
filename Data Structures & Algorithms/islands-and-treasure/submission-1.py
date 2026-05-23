class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c, 0))
            visited.add((r, c))

            while queue:
                r, c, d = queue.popleft()
                grid[r][c] = min(grid[r][c], d)
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r_new = r + dr
                    c_new = c + dc
                    if not (min(r_new, c_new) < 0 or
                            r_new == ROWS or
                            c_new == COLS or
                            (r_new, c_new) in visited or
                            grid[r_new][c_new] == -1):
                            queue.append((r_new, c_new, d + 1))
                            visited.add((r_new, c_new))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    bfs(i, j)
                    visited = set()

                        

        
        

                    