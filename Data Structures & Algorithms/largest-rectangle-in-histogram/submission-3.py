class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        area = 0
        stack = []

        for r in range(len(heights)):
            start = r
            while stack and stack[-1][0] > heights[r]:
                h, i = stack.pop()
                area = max((r-i) * h, area)
                start = i
            stack.append((heights[r], start))

        while stack:
            h, i = stack.pop()
            area = max(area, (len(heights)-i) * h)
        return area

