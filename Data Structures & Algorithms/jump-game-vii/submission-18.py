class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:


        if s[-1] == '1':
            return False
        
        dp = [False] * len(s)
        dp[0] = True
        j = 0
        for i in range(len(s)):
            if dp[i] == False:
                continue
            j = max(i+minJump, j)
            while j < min(i+maxJump+1, len(s)):
                if s[j] == '0':
                    dp[j] = True
                j += 1
    

        return dp[-1]
                

