class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        dp = {}


        def play(isAlice, M, i):
            if (isAlice, M, i) in dp:
                return dp[(isAlice, M, i)]
            if i == len(piles):
                return [0, 0]
            scores = [0, 0]
            curr = 0
            for j in range(i, min(i+2*M, len(piles))):
                newM = max(M, (j - i + 1))
                curr += piles[j]
                if isAlice:
                    sc = play(False, newM, j+1)
                    if (curr + sc[0]) > scores[0]:
                        scores = [curr+sc[0], sc[1]]
                else:
                    sc = play(True, newM, j+1)
                    if (curr + sc[1]) > scores[1]:
                        scores = [sc[0], curr+sc[1]]
            dp[(isAlice, M, i)] = scores
            return scores
    
        return play(True, 1, 0)[0]
            
        