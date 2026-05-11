class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total = sum(matchsticks)

        side = total / 4

        if side % 1 != 0:
            return False

        sides = [0] * 4
        
        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            matchsticks.sort(reverse=True)
            
            for j in range(4):
                if (sides[j] + matchsticks[i]) > side: 
                    continue
                sides[j] += matchsticks[i] 
                if dfs(i + 1):
                    return True
                sides[j] -=  matchsticks[i]

            return False
        
        return dfs(0)
        