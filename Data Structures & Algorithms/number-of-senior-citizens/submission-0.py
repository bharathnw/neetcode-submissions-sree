class Solution:
    def countSeniors(self, details: List[str]) -> int:

        cnt = 0

        for d in details:
            if int(d[-4] + d[-3]) > 60:
                cnt += 1
        
        return cnt
        