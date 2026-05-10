"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i, slot in enumerate(intervals):
            if i > 0:
                if slot.start < intervals[i - 1].end:
                    return False

        return True