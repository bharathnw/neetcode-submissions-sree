class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        out = []

        def dfs(i):
            if len(res) == k:
                out.append(res[:])
                return
            if i > n:
                return
            res.append(i)
            dfs(i+1)
            res.pop()
            dfs(i+1)

        dfs(1)
        return out        