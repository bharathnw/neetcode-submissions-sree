class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []
        res = []

        intervals.sort()

        res.append(intervals[0])

        for start, end in intervals[1:]:
            prevSt, prevEnd = res[-1]

            if start <= prevEnd:
                prevEnd = max(prevEnd, end)
                res[-1] = [prevSt, prevEnd]
            else:
                res.append([start, end])

        return res

        