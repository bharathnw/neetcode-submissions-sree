"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])
        res = 0
        l, r = 0,0
        count = 0
        while max(l,r) < len(intervals):
            if start[l] < end[r]:
                l += 1
                count += 1
            else:
                r += 1
                count -= 1
            res = max(count, res)
        
        return res

        