class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c, visited, dist):
            queue = deque()
            queue.append((r, c, 1))
            visited.add((r, c))

            while queue:
                r, c, d = queue.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r_new = r + dr
                    c_new = c + dc
                    if not (min(r_new, c_new) < 0 or
                            r_new == ROWS or
                            c_new == COLS or
                            (r_new, c_new) in visited or
                            grid[r_new][c_new] != INF):
                            queue.append((r_new, c_new, d + 1))
                            visited.add((r_new, c_new))
                            dist.append([(r_new, c_new), d])

        dists = {}
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visited = set()
                    dist = []
                    bfs(i, j, visited, dist)
                    dists[f"{i}, {j}"] = dist
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == INF:
                    # Get the treasure with minimum dist
                    min_d = 100
                    for chest in dists:
                        for point in dists[chest]:
                            # ex) [(1, 2), 0]
                            if point[0][0] == i and point[0][1] == j:
                                min_d = min(min_d, point[1])
                    grid[i][j] = min_d
                        

        
        

                    