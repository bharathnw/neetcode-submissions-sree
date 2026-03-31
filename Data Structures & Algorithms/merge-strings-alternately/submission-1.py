class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ''

        x, y = 0, 0

        while x < len(word1) and y < len(word2):
            res += word1[x]
            res += word2[y]
            x += 1
            y += 1
        
        if x < len(word1):
            res += word1[x:]
        if y < len(word2):
            res += word2[y:]
        
        return res