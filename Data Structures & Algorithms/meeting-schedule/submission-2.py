"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key= lambda i:i.start)

        for i in range(1, len(intervals)):
        
            start =  intervals[i].start

            if intervals[i-1].end > start:
                return False
        
        return True



