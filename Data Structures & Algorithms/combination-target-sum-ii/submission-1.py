class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        


        candidates.sort()
        res = []

        arr = []

        def backtrack(i, tot):
            if tot == target:
                res.append(arr[:])
                return
            if i == len(candidates) or tot > target:
                return
            arr.append(candidates[i])
            backtrack(i+1, tot+candidates[i])
            arr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, tot)

        backtrack(0, 0)
        return res