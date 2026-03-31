class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        out = []

        def combi(i):
            if len(out) == k:
                res.append(out[:])
                return
            if i == n+1:
                return
            out.append(i)
            combi(i+1)
            out.pop()
            combi(i+1)
        combi(1)
        return res