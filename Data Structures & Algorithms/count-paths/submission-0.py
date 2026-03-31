class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def findPath(r, c, preMap):
            if r < 0 or c < 0 or r == m or c == n:
                return 0
            if (r,c) in preMap:
                return preMap[(r,c)]
            if r == m-1 and c == n-1:
                return 1
            preMap[(r,c)] = findPath(r+1, c, preMap)+ findPath(r, c+1, preMap)
            return preMap[(r,c)]
        return findPath(0,0, {})
            
        