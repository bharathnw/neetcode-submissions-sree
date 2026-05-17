class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        i = 0
        res = []

        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        res.append(newInterval)
        curr = [res[0]]

        for st, end in res[1:]:
            if curr[-1][1] >= st:
                curr[-1] = [min(curr[-1][0], st), max(curr[-1][1], end)]
            else:
                curr.append([st, end])


        for st, end in intervals[i:]:
            if curr[-1][1] >= st:
                curr[-1] = [min(curr[-1][0], st), max(end, curr[-1][1])]
            else:
                curr.append([st,end])
        
        return curr
            


            
        