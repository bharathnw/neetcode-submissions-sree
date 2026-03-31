class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total = sum(stones)
        target = total//2

        maxTarget = 0

        dp = [False] * (target + 1)
        dp[0] = True

        for weight in stones:
            for currSum in range(target, weight-1, -1):
                if dp[currSum - weight] == True:
                    dp[currSum] = True
                    if dp[target] == True:
                        maxTarget = target
                        break
                    maxTarget = max(maxTarget, currSum)
        return total - (2 * maxTarget)
                




