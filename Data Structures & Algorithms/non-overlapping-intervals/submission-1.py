


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) <= 1:
            return 0
        intervals.sort()
        print(intervals)
        prev = intervals[0]
        count = 0
        for start, end in intervals[1:]:
            if prev[1] > start:
                count += 1
                prev[1] = min(end, prev[1])
            else:
                prev = [start, end]
        
        return count




        