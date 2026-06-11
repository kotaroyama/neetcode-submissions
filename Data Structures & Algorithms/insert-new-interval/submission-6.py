class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        new = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            new.append(intervals[i])
            i += 1
        
        # Case 1: we've appended all intervals
        if len(new) == len(intervals):
            new.append(newInterval)
            return new
        
        # Case 2: we've reached an interval whose start value
        #   is greater than the new interval's end
        if intervals[i][0] > newInterval[1]:
            new.append(newInterval)
            while i < len(intervals):
                new.append(intervals[i])
                i += 1
            return new

        # Case 3: there is an overlapping interval
        start = i
        while (i < len(intervals) and
            intervals[i][0] <= newInterval[1]):
            i += 1
        """
        if intervals[i][0] < newInterval[1]:
            new_item = [min(intervals[start][0], newInterval[0]),
                        max(intervals[i][1], newInterval[1])]
            i += 1
        else:
            new_item = [min(intervals[start][0], newInterval[0]),
                        max(intervals[i - 1][1], newInterval[1])]
        """
        new_item = [min(intervals[start][0], newInterval[0]),
                    max(intervals[i - 1][1], newInterval[1])]
        new.append(new_item)

        while i < len(intervals):
            new.append(intervals[i])
            i += 1

        return new