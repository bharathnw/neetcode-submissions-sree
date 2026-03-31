class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}

        def isMatching(i, j):
            if j == len(p):
                return i == len(s)
            
            if (i, j) in cache:
                return cache[(i,j)]
            
            firstMatch = i < len(s) and (p[j] == '.' or p[j] == s[i])
            
            if (j + 1) < len(p) and p[j+1] == '*':
                cache[(i, j)] = (firstMatch and isMatching(i+1, j)) or isMatching(i, j+2)
                return cache[(i, j)]
            else:
                if firstMatch:
                    cache[(i, j)] = isMatching(i+1, j+1)
                    return cache[(i, j)]
                else:
                    cache[(i, j)] = False
                    return False
        return isMatching(0,0)
            


