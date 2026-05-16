class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()

        def dfs(i, path, total):
            if total >= target or i >= len(candidates):
                path_copy = path.copy()
                if total == target and path_copy not in result:
                    result.append(path_copy)
                return     
            
            path.append(candidates[i])
            dfs(i + 1, path, total + candidates[i])

            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, path, total)

            
        
        dfs(0, path, 0)
        return result