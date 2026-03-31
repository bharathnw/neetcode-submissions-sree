class Solution:
    def numDecodings(self, s: str) -> int:
        checkSet = set(['0','1','2','3','4','5','6'])
        numSet = set()
        for i in range(1, 27):
            numSet.add(i)


        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for c in range(len(s)-1, -1, -1):
            ch = s[c]
            if ch == '0':
                dp[c] = 0
            else:
                dp[c] = dp[c+1]

            if c + 1 < len(s) and (s[c] == '1' or (s[c] == '2' and s[c+1] in checkSet)):
                dp[c] += dp[c+2]
        return dp[0]