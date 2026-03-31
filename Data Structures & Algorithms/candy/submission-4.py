class Solution:
    def candy(self, ratings: List[int]) -> int:

        leftRes = [1] *  len(ratings)
        rightRes = leftRes[:]

        for i in range(len(ratings)):
            if i > 0 and ratings[i-1] < ratings[i]:
                leftRes[i] = leftRes[i-1] + 1
        
        for i in range(len(ratings)-1, -1, -1):      
            if i < (len(ratings)-1) and ratings[i+1] < ratings[i]:
                rightRes[i] = rightRes[i+1] + 1

        res = 0
        for i in range(len(ratings)):
            res += max(leftRes[i], rightRes[i])

        return res
        