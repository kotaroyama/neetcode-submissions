class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        adj_list = {}
        for src, dst in edges:
            if src not in adj_list:
                adj_list[src] = []
            if dst not in adj_list:
                adj_list[dst] = []
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        
        def dfs(node, prev):
            if node in path:
                return False

            path.add(node)
            result = True
            for neighbor in adj_list[node]:
                if neighbor == prev:
                    continue
                result = result and dfs(neighbor, node)
            return result
        
        path = set()

        result = dfs(0, -1)
        if result and len(path) == n:
            return True
        
        return False

