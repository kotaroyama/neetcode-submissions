class CountSquares:

    def __init__(self):
        self.point_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            result += self.point_count[(x, py)] * self.point_count[(px, y)]
        return result