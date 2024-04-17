# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.numh=[]
        self.numl = []
        

    def addNum(self, num: int) -> None:

        if len(self.numl) == len(self.numh):
    

            if not self.numl or self.numh[0] >= num:
                heappush(self.numl,-num)
            else:
                heappush(self.numh,num)
                temp = heappop(self.numh)
                heappush(self.numl,-temp)

        else:
            if num >= -self.numl[0]:
                heappush(self.numh,num)

            else:
                heappush(self.numl,-num)
                temp = heappop(self.numl)
                heappush(self.numh,-temp)

    def findMedian(self) -> float:
       
        
        if len(self.numl) == len(self.numh):

            return (-self.numl[0] +self.numh[0])/2
        else:
            return (-self.numl[0])

        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()