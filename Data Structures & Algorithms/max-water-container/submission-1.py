class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount  = 0
        l , r = 0, len(heights)-1
        while l < r:
            amount = (r-l) * min(heights[r],heights[l])
            max_amount = max(amount, max_amount) 
            if heights[r] < heights[l]:
                r = r-1
            else: 
                l = l+1
        return max_amount