class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        output = 0
        if not height:
            return 0
        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                output += max(lMax - height[l], 0)
            else:
                r -= 1
                rMax = max(rMax, height[r])
                output += max(rMax - height[r], 0)
        return output
        