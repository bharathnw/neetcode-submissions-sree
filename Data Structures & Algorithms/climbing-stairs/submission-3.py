class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        prev = 1
        for i in range(n-1):
            temp = prev
            prev = last+prev
            last = temp
        
        return prev



        
    
