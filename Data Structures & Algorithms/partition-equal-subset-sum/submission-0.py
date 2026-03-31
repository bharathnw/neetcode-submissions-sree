class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        toFind = sum(nums)/2.0

        def dfs(index, total):
            if total == toFind:
                return True
            if index == len(nums) or total > toFind:
                return False
            
            #skip
            tot = dfs(index+1, total)

            if total + nums[index] <= toFind:
                #include
                if dfs(index+1, total + nums[index]) == True:
                    return True
            return tot
                
        
        return dfs(0, 0)
            

        