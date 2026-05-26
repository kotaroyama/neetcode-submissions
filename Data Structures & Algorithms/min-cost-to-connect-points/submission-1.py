class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj_list = {}
        for i in range(N):
            adj_list[i] = []
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append([j, weight])
                adj_list[j].append([i, weight])

        # Initialize the min-heap
        min_heap = [[0, 0]]
        total_cost = 0
        visited = set()

        while len(visited) < N:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            total_cost += cost
            visited.add(node)
            for neighbor, weight in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, [weight, neighbor])

        return total_cost
