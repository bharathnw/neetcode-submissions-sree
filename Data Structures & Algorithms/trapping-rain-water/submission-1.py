class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l <= r:
            if leftMax < rightMax:
                res += max(leftMax - height[l], 0)
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                res += max(rightMax - height[r], 0)
                rightMax = max(rightMax, height[r])
                r -= 1
        
        return res
                
