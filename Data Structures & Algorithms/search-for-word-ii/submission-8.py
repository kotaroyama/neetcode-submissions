class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        results = set()
        def dfs(i, j, node, seen, word):
            if (i < 0 or j < 0 or
                i == ROWS or j == COLS or
                (i, j) in seen or
                board[i][j] not in node.children):
                return
            
            seen.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.is_word:
                results.add(word)
            dfs(i + 1, j, node, seen, word)
            dfs(i, j + 1, node, seen, word)
            dfs(i - 1, j, node, seen, word)
            dfs(i, j - 1, node, seen, word)
            seen.remove((i, j))
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, set(), "")

        return list(results)