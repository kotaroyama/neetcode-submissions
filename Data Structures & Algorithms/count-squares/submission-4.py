class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            result += self.points[(x, y)] * self.points.get((x, py), 0) * self.points.get((px, y), 0)
        return result