class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        import sys
        sys.setrecursionlimit(100000)
        cache = {}
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            prefix[i] = prefix[i+1] + stoneValue[i]
        def playMax(isAlice, i):

            if i == len(stoneValue):
                return (0, 0)
            
            if (isAlice, i) in cache:
                return cache[(isAlice, i)]

            best = (-float('inf'), -float('inf'))

            for X in range(1, min(3, len(stoneValue)-i)+1):
                currSum = prefix[i] - prefix[i+X]
                if isAlice:
                    a, b = playMax(False, i+X)
                    score = a + currSum
                    if score > best[0]:
                        best = (score, b)
                else:
                    a, b = playMax(True, i+X)
                    score = b + currSum
                    if score > best[1]:
                        best = (a, score)
            cache[(isAlice, i)] = best
            return best
        
        a, b = playMax(True, 0)

        if a == b:
            return 'Tie'

        return 'Alice' if a > b else 'Bob'

        