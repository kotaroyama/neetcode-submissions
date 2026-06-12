class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        new = []
        item = [intervals[0][0], intervals[0][1]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= item[1]:
                item = [item[0], max(item[1], intervals[i][1])]
            else:
                new.append(item)
                item = [intervals[i][0], intervals[i][1]]
        
        new.append(item)
        
        return new