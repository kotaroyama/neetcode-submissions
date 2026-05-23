class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minutes = -1
        rotten = set()

        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
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
                            queue.append((r_new, c_new))
                            rotten.add((r_new, c_new))
            minutes += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        if minutes == -1:
            return 0
        return minutes