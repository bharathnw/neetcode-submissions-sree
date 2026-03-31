class Solution:
    def reverse(self, x: int) -> int:

        org = x

        x = abs(x)
        
        rotated = int(str(x)[::-1])

        if org < 0:
            rotated *= -1
        
        if rotated < -(1 << 31) or rotated > ((1 << 31) - 1):
            return 0
        
        return rotated
        