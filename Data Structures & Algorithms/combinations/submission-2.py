class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        arr = []

        def dfs(i):
            if len(arr) == k:
                res.append(arr[:])
                return
            if i == n+1:
                return
            arr.append(i)
            dfs(i+1)
            arr.pop()
            dfs(i+1)
        
        
        dfs(1)
        return res
        