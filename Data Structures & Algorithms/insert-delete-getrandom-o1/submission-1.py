class RandomizedSet:

    def __init__(self):
        self.vals = set()

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.vals.add(val)
        return True

    def remove(self, val: int) -> bool:
        try:
            self.vals.remove(val)
        except KeyError:
            return False
        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.vals) - 1)
        return list(self.vals)[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()