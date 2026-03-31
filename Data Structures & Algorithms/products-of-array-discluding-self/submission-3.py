class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        output = [1] * len(nums)
        for i in range(len(nums)):
            prefix[i] =  nums[i] * 1 if i == 0 else prefix[i-1] * nums[i]
        
        for i in reversed(range(len(nums))):
            postfix[i] = nums[i] * 1 if (i == len(nums) - 1) else postfix[i+1] * nums[i]
         

        for i in range(len(nums)):
            res = 1
            if i == 0:
               res = 1 * postfix[i+1]
            elif i == len(nums)-1:
                res = 1 * prefix[i - 1]
            else:
                res = postfix[i+1] * prefix[i-1]
            output[i] = res
        return output
            

        

        