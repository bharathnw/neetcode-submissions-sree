class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:


        if s[-1] == '1':
            return False
        
        dp = {}
        dp[len(s)-1] = True

        for i in range(len(s)-2, -1, -1):
            if s[i] == '1':
                dp[i] = False
                continue
            dp[i] = False
            for j in range(i+minJump, min(i+maxJump+1, len(s))):
                if dp[j] == True:
                    dp[i] = True
                    break

        return dp[0]
                

