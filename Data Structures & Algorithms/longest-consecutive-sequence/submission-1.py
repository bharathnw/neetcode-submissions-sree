class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        counter = set(nums)

        res = 0

        used = set()
        cnt = 0
        for num in nums:
            if num - 1 not in counter:
                res = 1
                temp = num
                while temp + 1 in counter:
                    res += 1
                    temp = temp + 1
                cnt = max(res, cnt)
        return cnt

        