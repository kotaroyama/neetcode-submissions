class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: set() for word in words for c in word}
        for i in range(0, len(words) - 1):
            if len(words[i]) > len(words[i + 1]) and words[i].startswith(words[i + 1]):
                return ""
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    adj[words[i][j]].add(words[i + 1][j])
                    break

        def dfs(src):
            if src in visited:
                return visited[src]
            visited[src] = True
            for neighbor in adj[src]:
                if dfs(neighbor):
                    return True
            result.append(src)
            visited[src] = False
            return False

        result = []
        visited = {}
        for c in adj:
            if dfs(c):
                return ""
        return "".join(result)[::-1]