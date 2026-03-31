class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if not digits:
            return 0
        res = digits[0]

        for num in digits[1:]:
            res = (res * 10) + num
        
        res += 1
        out = []
        while res > 0:
            out.append(res%10)
            res = res//10
        out.reverse()
        return out
        