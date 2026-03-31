# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        res = []

        for i in range(len(pairs)):
            temp = pairs[i]
            bef = i - 1

            while bef >= 0 and pairs[bef].key > temp.key:
                pairs[bef+1] = pairs[bef]
                bef -= 1
            pairs[bef+1] = temp
            res.append(pairs[:])

        return res