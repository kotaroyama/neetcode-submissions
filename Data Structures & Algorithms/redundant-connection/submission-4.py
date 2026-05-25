class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = {}
        for n1, n2 in edges:
            if n1 not in adj_list:
                adj_list[n1] = []
            if n2 not in adj_list:
                adj_list[n2] = []
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        def dfs(node, prev):
            nonlocal cycle_start

            if node in visited:
                cycle_start = node
                return True
            
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == prev:
                    continue
                if dfs(neighbor, node):
                    if cycle_start != -1:
                        cycle.add(node)
                    if node == cycle_start:
                        cycle_start = -1
                    return True
            return False

        cycle_start = -1
        cycle = set()
        visited = set()

        dfs(1, -1)

        for n1, n2 in reversed(edges):
            if n1 in cycle and n2 in cycle:
                return [n1, n2]

        

