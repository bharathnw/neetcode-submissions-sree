class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res = ''

        carry = 0
        for i in range(1, max(len(a), len(b))+1):
            
           pA = 0 if i > len(a) else int(a[-i])
           pB = 0 if i > len(b) else int(b[-i])
           tot = pA+pB+carry
           res = str(tot%2) + res
           carry = tot//2

        
        if carry > 0:
            res = '1' + res
        return res