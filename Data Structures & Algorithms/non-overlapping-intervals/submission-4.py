class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals or len(intervals) <= 1:
            return 0

        intervals.sort()


        curr = intervals[0]

        res = 0

        for st, en in intervals[1:]:

            if curr[1] > st:
                res += 1
                curr = [st, min(en, curr[1])]
            else:
                curr = [st, en]
        
        return res




        