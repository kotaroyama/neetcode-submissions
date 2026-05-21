class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        count = 0
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    if not (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or
                        c + dc == COLS or
                        (r + dr, c + dc) in visited or
                        grid[r + dr][c + dc] == "0"):
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))    


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    bfs(i, j)

        return count