class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums or len(nums) == 0:
                return 0
        if len(nums) == 1:
                return nums[0]
        
        def helper(arr):
            if not arr or len(arr) == 0:
                return 0
            if len(arr) == 1:
                return arr[0]

            cache = {}
            cache[0] = arr[0]
            cache[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                cache[i] = max(cache[i-2] + arr[i], cache[i-1])
            
            return cache[len(arr)-1]
                
        

        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))
        