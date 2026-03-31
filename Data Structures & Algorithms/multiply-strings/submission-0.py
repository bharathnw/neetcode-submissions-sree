class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1,-1,-1):
            for i2 in range(len(num2)-1,-1,-1):
                mul = int(num1[i]) * int(num2[i2]) 
                p1 = i + i2
                p2 = p1 + 1
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
        
        out = ""
        for i, num in enumerate(res):
            if i == 0 and num == 0:
                continue
            out += str(num)
        return out


                    
                
                



        
        