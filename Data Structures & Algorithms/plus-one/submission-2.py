class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if not digits:
            return 1

        res = digits[0]

        for digit in digits[1:]:
            res = (res * 10) + digit
        res += 1
        resArr = []
        while res > 0:
            rem = res % 10
            res = res // 10
            resArr.append(rem)
        
        return resArr[::-1]

        