class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        nums.sort()

        for i, num in enumerate(nums):
            diff = 0-num
            l,r = i+1, len(nums)-1
            while l<r:
                if nums[l]+nums[r] < diff:
                    l+=1
                elif nums[l]+nums[r] > diff:
                    r -= 1
                else:
                    result_set.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
        print(result_set)
        return list(result_set)