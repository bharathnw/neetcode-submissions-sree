class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        counter = {}

        if len(hand) % groupSize != 0:
            return False

        for h in hand:
            counter[h] = counter.get(h, 0) + 1
        


        for h in hand:
            start = h
            while (start-1) in counter and counter[start - 1] > 0:
                start = start - 1
            
            if counter[start] <= 0:
                continue

            for g in range(groupSize):
                if start + g in counter and counter[start + g] > 0:
                    counter[start + g] -= 1
                else:
                    return False
        
        return True
