class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build an adj list: (destination, price)
        adj_list = {}
        for i in range(0, n):
            adj_list[i] = []
        for s, d, price in flights:
            adj_list[s].append([d, price])
        
        # Create the INF list
        INF = float("inf")
        dist = [[INF] * (k + 5) for _ in range(n)]
        
        dist[src][0] = 0
        min_heap = [[0, src, -1]] #[total_price, origin, total_stops]
        while min_heap:
            p1, n1, stop1 = heapq.heappop(min_heap)
            if n1 == dst: return p1
            if stop1 == k or dist[n1][stop1 + 1] < p1:
                continue
            for airport in adj_list[n1]:
                n2 = airport[0]
                p2 = airport[1]
                stop2 = 1 + stop1
                if dist[n2][stop2 + 1] > p1 + p2:
                    dist[n2][stop2 + 1] = p1 + p2
                    heapq.heappush(min_heap, (p1 + p2, n2, stop2))

        return -1