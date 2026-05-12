class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(l, r, isAlice):
            if (l, r, isAlice) in dp:
                return dp[(l, r, isAlice)]
            if l > r:
                return 0
            if isAlice:
                dp[(l, r, isAlice)] = max(piles[l] + dfs(l+1, r, False), piles[r] + dfs(l, r-1, False))
                return dp[(l, r, isAlice)]
            else:
                dp[(l, r, isAlice)] = min(-piles[l] + dfs(l+1, r, True), -piles[r] + dfs(l, r-1, True))
                return dp[(l, r, isAlice)]
        
        return dfs(0, len(piles)-1, True) > 0