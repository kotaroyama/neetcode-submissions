class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):
            count = 1
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            
            while queue:
                r, c = queue.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for rd, cd in directions:
                    if ((r + rd, c + cd) not in visited and
                        min(r + rd, c + cd) >= 0 and
                        (r + rd) < ROWS and
                        (c + cd) < COLS and
                        grid[r + rd][c + cd] == 1):
                        queue.append((r + rd, c + cd))
                        visited.add((r + rd, c + cd))
                        count += 1
            
            return count


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, bfs(i, j))

        return max_area