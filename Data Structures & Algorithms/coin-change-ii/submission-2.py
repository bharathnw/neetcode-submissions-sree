class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {}

        def dfs(i, tot):
            if tot > amount or i == len(coins):
                return 0
            if tot == amount:
                return 1
            if (i, tot) in dp:
                return dp[(i, tot)]
            res = 0
            for j in range(i,len(coins)):
                res += dfs(j, tot+coins[j])
            dp[(i, tot)] = res
            return res

        return dfs(0, 0)
            