class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        curr = 0 
        fast = 0

        while True:
            fast = nums[nums[fast]]
            curr = nums[curr]
            if curr == fast:
                break
        
        curr2 = 0
        while True:
            curr = nums[curr]
            curr2 = nums[curr2]
            if curr == curr2:
                return curr2

        