class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build an adj list: (destination, time)
        adj_list = {}
        for i in range(1, n + 1):
            adj_list[i] = []
        for src, dst, time in times:
            adj_list[src].append([dst, time])
        
        shortest = {}
        min_heap = [[0, k]]
        while min_heap:
            t1, n1 = heapq.heappop(min_heap)
            if n1 in shortest:
                continue
            shortest[n1] = t1
            for node in adj_list[n1]:
                n2 = node[0]
                t2 = node[1]
                if n2 not in shortest:
                    heapq.heappush(min_heap, (t1 + t2, n2))

        if len(shortest) != n:
            return -1
        total_time = -1
        for i in shortest:
            total_time = max(total_time, shortest[i])
        return total_time
        



