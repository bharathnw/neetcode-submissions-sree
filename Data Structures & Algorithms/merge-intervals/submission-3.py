class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        mapper = defaultdict(int)

        for st, end in intervals:
            mapper[st] += 1
            mapper[end] -= 1
        
        interval = []
        res = []
        have = 0
        for i in sorted(mapper):
            if not interval:
                interval.append(i)
            
            have += mapper[i]
            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        
        return res
        