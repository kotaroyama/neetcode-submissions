class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        results = []

        trie = {}
        for word in words:
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['#'] = word

        def dfs(i, j, node, seen):
            if '#' in node:
                results.append(node.pop('#'))
            
            if (i < 0 or i >= ROWS or
                j < 0 or j >= COLS or
                (i, j) in seen
                or board[i][j] not in node):
                return
            
            char = board[i][j]
            seen.add((i, j))
            dfs(i + 1, j, node[char], seen)
            dfs(i, j + 1, node[char], seen)
            dfs(i - 1, j, node[char], seen)
            dfs(i, j - 1, node[char], seen)
            seen.remove((i, j))
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, trie, set())

        return results