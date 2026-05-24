class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create adj list
        adj_list = {}
        for src, dst in prerequisites:
            if src not in adj_list:
                adj_list[src] = []
            if dst not in adj_list:
                adj_list[dst] = []
            adj_list[src].append(dst)

        for course in range(numCourses):
            if course not in adj_list:
                adj_list[course] = []
        
        def dfs(node, path):
            if not adj_list[node]:
                if node not in path:
                    path.append(node)
                return True
            if node in visited:
                path = []
                return False

            visited.add(node)
            result = True
            for neighbor in adj_list[node]:
                result = result and dfs(neighbor, path)
            if not result:
                return False
            if path and node not in path:
                path.append(node)
            visited.remove(node)
            return result
            
        visited = set()
        path = []
        print(adj_list)
        for course in adj_list:
            result = dfs(course, path)
            if not result:
                return []

        return path
