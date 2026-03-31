class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)
        def partitions(i, tot, k):
            if k == 0:
                return True
            if tot == target:
                return partitions(0, 0, k-1)
            
            for j in range(i,len(nums)):
                if used[j] == 1 or (tot + nums[j]) > target:
                    continue
                used[j] = 1
                if partitions(j+1, tot+nums[j], k):
                    return True
                used[j] = 0
            return False
        
        return partitions(0, 0, k)
            
        