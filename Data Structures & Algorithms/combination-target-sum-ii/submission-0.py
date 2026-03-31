class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(currSum, index, arr):
            if currSum == target:
                res.append(arr[:])
                return
            if index == len(candidates):
                return 

            if currSum > target:
                return
            currCan = candidates[index]        
            arr.append(currCan)
            dfs(currSum+currCan, index+1, arr)
            arr.pop()
            while index + 1 < len(candidates) and currCan == candidates[index+1]:
                index += 1
            dfs(currSum, index+1, arr)
        
        dfs(0, 0, [])
        return res

        