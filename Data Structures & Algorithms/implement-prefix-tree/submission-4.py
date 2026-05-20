class PrefixTree:

    def __init__(self):
        self.words = []

    def insert(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        for w in self.words:
            if word == w:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.words:
            if prefix == word[:len(prefix)]:
                return True
        return False
        