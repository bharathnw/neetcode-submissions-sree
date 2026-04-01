class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] >= x:
                res[-1][1] = max(y, res[-1][1])
            else:
                res.append([x, y])
            

        return res
