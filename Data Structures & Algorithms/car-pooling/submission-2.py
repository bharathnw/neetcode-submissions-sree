class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key=lambda x:x[1])

        currCap = trips[0][0]
        currDest = trips[0][2]


        for trip in trips[1:]:
            if trip[1] < currDest:
                if currCap + trip[0] <= capacity:
                    currCap += trip[0]
                else:
                    return False
            else:
                currCap = trip[0]
                currDest = trip[2]
        
        return True
        