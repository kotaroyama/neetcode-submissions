class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minutes = 0
        rotten = set()

        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        while queue:
            r, c, d = queue.popleft()
            rotten.add((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                r_new = r + dr
                c_new = c + dc
                if not (min(r_new, c_new) < 0 or
                        r_new == ROWS or
                        c_new == COLS or
                        (r_new, c_new) in rotten or
                        grid[r_new][c_new] == 0) and grid[r_new][c_new] == 1:
                        grid[r_new][c_new] = 2
                        queue.append((r_new, c_new, d + 1))
                        rotten.add((r_new, c_new))
            minutes = d
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return minutes