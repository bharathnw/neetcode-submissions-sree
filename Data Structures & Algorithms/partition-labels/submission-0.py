class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        charPositions = {}
        res = []

        for i in range(len(s)):
            charPositions[s[i]] = i
        

        R = len(s)

        l, r = 0, charPositions[s[0]] 
        while r < R:
            count = 0
  
            while l <= r:
                r = max(r, charPositions[s[l]])
                count += 1
                l += 1
                if l == R:
                    break
            res.append(count)
            if l == R:
                break
            r = charPositions[s[l]]


        return res