class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        res = 0
        currEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if currEnd > start:
                res += 1
                currEnd = min(currEnd, end)
                continue
            currEnd = end

        return res
        