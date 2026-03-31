class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = sum(matchsticks)
        if n % 4 != 0:
            return False
        
        l = n // 4

        for stick in matchsticks:
            if stick > l:
                return False
            
        sides = [0] * 4
        def backTrack(i):
            if i == len(matchsticks):
                return sides[0]== sides[1] == sides[2]== sides[3]
            
            for j in range(4):
                sides[j] += matchsticks[i]

                if sides[j] <= l and backTrack(i+1) == True:
                    return True

                sides[j] -= matchsticks[i]
            
            return False
        
        return backTrack(0)