class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)== 1:
            return nums[0]
        def dfs(i, arr, cache):
            if i in cache:
                return cache[i]
            if i >= len(arr):
                return 0
            cache[i] = max(dfs(i+1, arr, cache), arr[i] + dfs(i+2, arr, cache))
            return cache[i]

        return max(dfs(0, nums[1:], {}), dfs(0, nums[:len(nums)-1], {}))
        