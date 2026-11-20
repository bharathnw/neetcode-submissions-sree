class UndergroundSystem:
    def __init__(self):
        self.tickets = {}
        self.completed_trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.tickets:
            return
        self.tickets[id] = [(stationName, t)]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        if id not in self.tickets:
            return 
        in_ticket = self.tickets[id][0]
        if (in_ticket[0], stationName) in self.completed_trips:
            self.completed_trips[(in_ticket[0], stationName)].append((id, in_ticket[1], t))
        else:
            self.completed_trips[(in_ticket[0], stationName)] = [((id, in_ticket[1], t))]
        
        del self.tickets[id]

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        trips = self.completed_trips[(startStation, endStation)]

        if not trips:
            return 

        n = len(trips)

        tot = 0

        for _, in_time, out_time in trips:

            tot += (out_time - in_time)
        print((tot / n))
        return (tot / n)
    

