class Solution:
    def partitionString(self, s: str) -> int:
        
        visits = set()
        res = 1
        for c in s:
            if c in visits:
                res += 1
                visits.clear()
            visits.add(c)
        
        return res
