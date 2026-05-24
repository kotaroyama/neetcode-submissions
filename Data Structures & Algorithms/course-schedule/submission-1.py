class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adj list
        adj_list = {}
        for src, dst in prerequisites:
            if src not in adj_list:
                adj_list[src] = []
            if dst not in adj_list:
                adj_list[dst] = []
            adj_list[src].append(dst)
        
        def dfs(node, adj_list, path):
            if node in path:
                return False
            if not adj_list[node]:
                return True
            
            path.add(node)
            result = True
            for neighbor in adj_list[node]:
                result = result and dfs(neighbor, adj_list, path)
            path.remove(node)
            return result

        for course in adj_list:
            path = set()
            result = dfs(course, adj_list, path)
            if not result:
                print(adj_list)
                print(course)
                return False
        
        return True
