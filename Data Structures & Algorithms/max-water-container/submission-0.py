class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        max_amount = 0
        l = 0
        r = len(heights)-1

        while l < r:
            area = min(heights[l],heights[r]) * (r-l)
            max_amount = max(max_amount,area )

            if heights[l] >= heights[r]:
                r = r-1
            else:
                l +=1

        return max_amount