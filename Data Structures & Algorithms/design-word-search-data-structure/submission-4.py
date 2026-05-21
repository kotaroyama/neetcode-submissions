class LetterNode:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = LetterNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = LetterNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        
        def dfs(word, curr):
            if len(word) == 0 and curr.children:
                return curr.end_of_word
            if len(word) == 0:
                return curr.end_of_word
            
            for i, c in enumerate(word):
                if not curr.children:
                    return False
                if c not in curr.children and c != ".":
                    return False
                if c == ".":
                    result = False
                    for child in curr.children:
                        result = result or dfs(word[i+1:], curr.children[child])
                    return result
                else:
                    curr = curr.children[c]
            return curr.end_of_word

        curr = self.root

        return dfs(word, curr)
        
