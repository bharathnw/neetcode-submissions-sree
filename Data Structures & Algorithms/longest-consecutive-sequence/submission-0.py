class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        out = []
        for num in nums:
            num_set.add(num)
        
        for num in num_set:
            if num - 1 not in num_set:
                val = num
                res = []
                res.append(val)
                while 1+val in num_set:
                    val = 1+val
                    res.append(val)
                if len(res) > len(out):
                    out = res
        return len(out)
                    