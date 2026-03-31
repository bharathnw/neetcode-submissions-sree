class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        res = []
        def twoSumDistinctPairs(arr, goal):
            L, R = 0, len(arr)-1
            res = []
            while L < R:
                if arr[L] + arr[R] < goal:
                    L += 1
                elif arr[L] + arr[R] > goal:
                    R -= 1
                else:
                    L += 1
                    R -= 1
                    res.append((arr[L], arr[R]))
                    while L < R and arr[L] == arr[L-1]:
                        L += 1
                    while L < R and arr[R] == arr[R+1]:
                        R -= 1
            return res
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                L, R = j+1, len(nums)-1
                while L < R:
                    total = nums[i] + nums[j] + nums[L] + nums[R]
                    if total < target:
                        L += 1
                    elif total > target:
                        R -= 1
                    else:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L-1]:
                            L += 1
                        while L < R and nums[R] == nums[R+1]:
                            R -= 1
        
        return res







                    

                    
