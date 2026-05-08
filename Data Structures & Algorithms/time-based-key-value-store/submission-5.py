class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            vals = []
            vals.append([value, timestamp])
            self.values[key] = vals
        else:
            self.values[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.values:
            return ""
        if key not in self.values:
            return ""
        
        values = self.values[key].copy()
        # Get the most recent timestamp
        result = ""
        L = 0
        R = len(values) - 1
        while L <= R:
            mid = (L + R) // 2
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                L = mid + 1
            else:
                R = mid - 1
        
        return result
        
