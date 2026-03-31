class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hands = {}
        for h in hand:
            hands[h] = hands.get(h, 0) + 1
        
        for h in hand:
            start = h
            while start-1 in hands and hands[start-1] > 0:
                start = start - 1
            
            if hands[start] <= 0:
                continue
            
            for i in range(start, start+groupSize):
                if i not in hands or hands[i] <= 0:
                    return False
                
                hands[i] -= 1
        
        return True