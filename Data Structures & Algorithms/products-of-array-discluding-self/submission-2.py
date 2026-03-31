class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_product = [1]*length
        right_product= [1]*length
        for i in range(1,length):
            left_product[i] = left_product[i-1]*nums[i-1]
        
        for j in range(length-2,-1,-1):
            print(j)
            right_product[j] = right_product[j+1]*nums[j+1]

        print( right_product)
        return [num1*num2 for num1,num2 in zip(left_product,right_product)]
            

