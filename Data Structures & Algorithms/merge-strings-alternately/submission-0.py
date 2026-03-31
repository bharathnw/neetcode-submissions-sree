class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ''

        while i < min(len(word1), len(word2)):
            res += word1[i]
            res += word2[i]
            i += 1
        
        if i < len(word1):
            res += word1[i: len(word1)]
        elif i < len(word2):
            res += word2[i: len(word2)]

        return res        
        