class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        res = [0,0,0]
        for card in triplets:
            if card[0] > target[0] or card[1] > target[1] or card[2] > target[2]:
                continue
            res[0] = max(card[0], res[0])
            res[1] = max(card[1], res[1])
            res[2] = max(card[2], res[2])
        
        return res == target

        