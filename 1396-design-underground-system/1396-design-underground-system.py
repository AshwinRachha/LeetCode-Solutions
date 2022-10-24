class UndergroundSystem:

    def __init__(self):
        
        self.log = {}
        
        self.journeys = {}
                
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.log[id] = [stationName, t]

    def checkOut(self, id: int, end_station: str, t: int) -> None:

        start_station, start_time = self.log.pop(id)
        journey = (start_station, end_station)
        if journey not in self.journeys:
            self.journeys[journey] = [0, 0]
        self.journeys[journey][0] += (t - start_time)
        self.journeys[journey][1] += 1
            
    def getAverageTime(self, start_station: str, end_station: str) -> float:
        total_time, total_trips = self.journeys[(start_station, end_station)]
        return total_time / total_trips