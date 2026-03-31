class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        L, R = float('inf'), float('-inf')

        for _, fro, to in trips:
            L = min(L, fro)
            R = max(R, to)
        
        dis = R - L + 1

        track = [0] * (dis + 1)

        for cap, fro, to in trips:
            track[fro-L] += cap
            track[to-L] -= cap
        currCap = 0
        for cap in track:
            currCap += cap
            if currCap > capacity:
                return False
        
        return True
        