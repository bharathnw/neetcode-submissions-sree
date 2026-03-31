class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def searchTarget(l, r):
            m = (l+r)//2
            if l > r:
                return -1
            if target == nums[m]:
                return m
            elif target < nums[m]:
                return searchTarget(l, r-1)
            elif target > nums[m]:
                return searchTarget(m+1, r)
            
            
        
        val = searchTarget(0, len(nums)-1)
        return val
        
        