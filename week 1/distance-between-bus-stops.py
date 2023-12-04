class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        r1=0
        r2=0
        i=start
        j=start
        while i%len(distance)!=destination:
            r1+=distance[i%len(distance)]
            
            i+=1
        while j%len(distance)!=destination:
            r2+=distance[j-1]
            j-=1
        return(min(r1,r2))


 

        