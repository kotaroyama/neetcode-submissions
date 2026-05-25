class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}

        for n1, n2 in edges:
            if n1 not in adj_list:
                adj_list[n1] = []
            if n2 not in adj_list:
                adj_list[n2] = []
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        def dfs(node, prev):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == prev:
                    continue
                dfs(neighbor, node)


        count = 0
        visited = set()
        prev = -1
        for node in adj_list:
            if node in visited:
                continue
            dfs(node, prev)
            prev = node
            count += 1

        count += (n - len(visited))

        return count
        
        