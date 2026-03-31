class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        sMap = {}

        for c in s1:
            sMap[c] = sMap.get(c, 0) + 1
        
        currWindow = {}
        L = 0
        for R in range(len(s2)):
            currWindow[s2[R]] = currWindow.get(s2[R],0) + 1

            if R - L + 1 > len(s1):
                currWindow[s2[L]] -= 1
                if currWindow[s2[L]] == 0:
                    del currWindow[s2[L]]
                L += 1
            
            if currWindow == sMap:
                return True
        
        return False

        