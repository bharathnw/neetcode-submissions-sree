class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adj = set()

        for tr in trust:
            if tr[1] not in adj:
                adj.add(tr[1])

        if len(adj) == 1:
            return list(adj)[0]
        else:
            return -1
