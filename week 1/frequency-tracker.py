class FrequencyTracker:

    def __init__(self):
        self.tracked=defaultdict(int)
        self.fre=defaultdict(int)
        

    def add(self, number: int) -> None:
        if self.fre[self.tracked[number]]!=0:
            self.fre[self.tracked[number]]-=1
        self.tracked[number]+=1
        
        self.fre[self.tracked[number]]+=1
    def deleteOne(self, number: int) -> None:
        if self.tracked[number]!=0:
            self.fre[self.tracked[number]]-=1

            self.tracked[number]-=1
            
            self.fre[self.tracked[number]]+=1

        

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.fre and self.fre[frequency]!=0:
            return True
        else:
            return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)