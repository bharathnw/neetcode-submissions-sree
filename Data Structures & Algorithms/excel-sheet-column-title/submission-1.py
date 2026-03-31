class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        res = ''

        if columnNumber <= 26:
            return chr(ord('A') + columnNumber - 1)
        
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            res += chr(ord('A') + rem)
            columnNumber //= 26
        
        return res[::-1]

        