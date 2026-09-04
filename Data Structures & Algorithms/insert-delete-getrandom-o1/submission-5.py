class RandomizedSet:

    def __init__(self):
        self.set_map = {}
        self.set_list = []

    def insert(self, val: int) -> bool:
        result = val not in self.set_map
        if result:
            self.set_list.append(val)
            self.set_map[val] = len(self.set_list) - 1
        return result

    def remove(self, val: int) -> bool:
        result = val in self.set_map
        if result:
            index = self.set_map[val]
            self.set_list[index] = self.set_list[-1]
            self.set_map[self.set_list[-1]] = index
            self.set_list.pop()
            del self.set_map[val]
        return result

    def getRandom(self) -> int:
        return random.choice(self.set_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()