class Solution:
    def candy(self, ratings: List[int]) -> int:

        leftCandy = [1] * len(ratings)
        rightCandy = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                leftCandy[i] = leftCandy[i-1] + 1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rightCandy[i] = rightCandy[i+1] + 1
        
        res = 0
        for i in range(len(ratings)):
            res += max(leftCandy[i], rightCandy[i])
        
        return res
        

        