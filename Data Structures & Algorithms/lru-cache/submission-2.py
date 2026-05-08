class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.order = []
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key in self.hash_map:
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            return self.hash_map[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if self.size < self.capacity and key not in self.hash_map:
            self.order.append(key)
            self.hash_map[key] = value
            self.size += 1
        elif key in self.hash_map:
            self.hash_map[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            key_remove = self.order[0]
            del self.hash_map[key_remove]
            self.order.remove(key_remove)
            self.order.append(key)
            self.hash_map[key] = value


class DDL:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

