class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[2])
        n=len(trips)-1
        sul=[0]*(trips[n][2]+1)
        for i in range(len(trips)):
            sul[trips[i][1]]+=trips[i][0]
            sul[trips[i][2]]-=trips[i][0]
        for i in range(1,len(sul)):
            sul[i]+=sul[i-1]
        for i in range(len(sul)):
            if sul[i]>capacity:
                return False
        return True

        
        

    
        