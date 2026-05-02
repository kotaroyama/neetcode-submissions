class MinStack:

    def __init__(self):
        self.vals = []  
        self.min_heap = []

    def push(self, val: int) -> None:
        self.vals.append(val)

    def pop(self) -> None:
        self.vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return min(self.vals)
