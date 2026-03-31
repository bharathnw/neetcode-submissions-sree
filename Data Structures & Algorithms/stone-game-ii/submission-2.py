class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        cache = {}

        def calc(isAlice, i, M):
            if i == len(piles):
                return (0, 0)
            
            key = (isAlice, i, M)
            if key in cache:
                return cache[key]
            
            res = (0,0)
            for j in range(1, min(len(piles)-i, 2*M)+1):
                total = sum(piles[i:i+j])
                alice, bob = calc(not isAlice, i+j, max(M, j))

                if isAlice:
                    alice += total
                    if alice > res[0]:
                        res = (alice, bob)
                else:
                    bob += total
                    if bob > res[1]:
                        res = (alice, bob)
            cache[key] = res       
            return res
        
        return calc(True, 0, 1)[0]

