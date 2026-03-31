class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        currCapacity = 0
        currEnd = 0
        trips_sorted = sorted(trips, key=lambda trip: trip[1])
        for trip in trips_sorted:
            if trip[1] >= currEnd:
                currCapacity = trip[0]
                currEnd = trip[2]
            else:
                currCapacity += trip[0]
                currEnd = trip[2]
            if currCapacity > capacity:
                return False
        
        return True
        