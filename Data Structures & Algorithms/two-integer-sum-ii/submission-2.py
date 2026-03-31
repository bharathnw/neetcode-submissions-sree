class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = defaultdict(int)

        for index,value in enumerate(numbers):
            req = target-value
            if value == req:
                continue
            if  res[req]:
                return [res[req],index+1]
            else:
                res[value] = index+1
            
        
        