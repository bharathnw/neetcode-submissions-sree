class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)

        if total % k != 0:
            return False

        target = (total)//k
        visits = [False] * len(nums)
        nums.sort(reverse=True)

        def dfs(ko, i, currSum):
            if ko == 0:
                return True
            if currSum == target:
                return dfs(ko-1, 0, 0)
            
            for j in range(i, len(nums)):
                if visits[j] == False and (currSum + nums[j]) <= target:
                    visits[j] = True
                    if dfs(ko, j+1, currSum+nums[j]):
                        return True
                    visits[j] = False
            
            return False
        
        return dfs(k, 0, 0)
        


                
