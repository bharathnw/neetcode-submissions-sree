class Solution:
    def heightChecker(self, heights: List[int]) -> int:


        h_sorted = sorted(heights)

        res = 0

        for i in range(len(heights)):
            if heights[i] != h_sorted[i]:
                res += 1
        
        return res
        

        