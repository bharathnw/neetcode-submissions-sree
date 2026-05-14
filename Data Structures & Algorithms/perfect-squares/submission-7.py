class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = []

        for i in range(n+1):
            dp.append(i)
        
        for num in range(1, n+1):
            for i in range(1, n+1):
                if num - (i*i) < 0:
                    break
                dp[num] = min(1 + dp[num-(i*i)], dp[num])

        return dp[-1]
                
                

                



            

            
            
        