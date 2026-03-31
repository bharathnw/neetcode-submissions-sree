class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]
        
        n = len(intervals)

        for index, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                intervals.insert(index, newInterval)
                break
            elif intervals[0] == newInterval[0]:
                intervals[index] = [newInterval[0], max(newInterval[1], interval[1])]
                break
        
        if len(intervals) == n:
            intervals.append(newInterval)
        
        res = [intervals[0]]
        for st, end in intervals[1:]:
            prevS, prevE = res[-1]
            if prevE >= st:
                res[-1] = [min(prevS, st), max(end, prevE)]
            else:
                res.append([st, end])
        
        return res


        

        