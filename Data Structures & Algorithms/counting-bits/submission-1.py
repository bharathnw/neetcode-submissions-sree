class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        counter = 1
        for i in range(1, n+1):
            res.append(1+res[i-counter])
            if i == counter:
                counter *= 2
        
        return res
            


            

