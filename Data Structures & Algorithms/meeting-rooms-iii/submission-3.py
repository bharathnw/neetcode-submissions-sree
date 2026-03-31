class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        available = []
        room_ledger = {}
        occupied = []

        for i in range(n):
            heapq.heappush(available, i)
            room_ledger[i] = 0
        
        meetings.sort()

        for start, end in meetings:

            while occupied and occupied[0][0] < start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
            
            if not available:
                w_end, w_room = heapq.heappop(occupied)

                if start < w_end:
                    heapq.heappush(occupied, (w_end + (end-start), w_room))
                else:
                    heapq.heappush(occupied, (w_end, w_room))

                room_ledger[w_room] += 1

            else:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
                room_ledger[room] += 1
        
        res = 0
        max_item = 0
        for room, cnt in room_ledger.items():
            if cnt > max_item:
                res = room
                max_item = cnt
        
        return res



            
            

            

            
        
    
        