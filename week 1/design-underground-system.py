class UndergroundSystem:

    def __init__(self):
        self.start={}
        self.destination=defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        self.destination[(self.start[id][0],stationName)].append(t-self.start[id][1])
        


        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ans=self.destination[(startStation,endStation)]

        return sum(ans)/len(ans)

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)