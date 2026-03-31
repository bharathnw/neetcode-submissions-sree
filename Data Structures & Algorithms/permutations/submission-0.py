class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        com = {}

        for i in range(len(nums)):
            com[i] = False
        res = []
        def backtrack(index, arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            for i in range(len(nums)):
                if com[i] == True:
                    continue
                com[i] = True
                arr.append(nums[i])
                backtrack(i, arr)
                arr.pop()
                com[i] = False
        backtrack(0, [])
        return res





            



        