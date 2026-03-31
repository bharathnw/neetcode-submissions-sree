class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        newSet = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                newSet.remove(nums[L])
                L += 1
            if nums[R] in newSet:
                return True
            newSet.add(nums[R])
        return False



                
            

        