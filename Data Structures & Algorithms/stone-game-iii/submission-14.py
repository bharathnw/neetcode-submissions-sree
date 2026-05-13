class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        dp = {len(stoneValue) : 0}

        for i in range(len(stoneValue)-1, -1, -1):
            res =  float('-inf')
            tot = 0
            for j in range(i, min(i+3, len(stoneValue))):
                tot += stoneValue[j]
                res = max(res, tot - dp[j+1])
            
            dp[i] = res

        res = dp[0]

        if res == 0:
            return 'Tie'
        return 'Alice' if res > 0 else 'Bob' 




        