class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}

        def findMax(M, i, isAlice):
            if i == len(piles):
                return (0, 0)

            key = (M, i, isAlice)
            if key in cache:
                return cache[key]

            res = (0, 0)

            for X in range(1, min(len(piles) - i, 2*M) + 1):
                currSum = sum(piles[i:i+X])

                if isAlice:
                    currScore = findMax(max(X, M), i + X, False)
                    score = (currScore[0] + currSum, currScore[1])
                    if score[0] > res[0]:
                        res = score
                else:
                    currScore = findMax(max(X, M), i + X, True)
                    score = (currScore[0], currScore[1] + currSum)
                    if score[1] > res[1]:
                        res = score

            cache[key] = res
            return res


        return findMax(1, 0, True)[0]


            