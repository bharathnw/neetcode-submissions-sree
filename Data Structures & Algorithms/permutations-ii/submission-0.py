class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = set()
        visits = set()
        n = len(nums)


        def dfs(arr):
            if len(arr) == n:
                res.add(tuple(arr[:]))
                return
            for i in range(n):
                if i not in visits:
                    visits.add(i)
                    arr.append(nums[i])
                    dfs(arr)
                    arr.pop()
                    visits.remove(i)
        dfs([])
        return list(res)
        