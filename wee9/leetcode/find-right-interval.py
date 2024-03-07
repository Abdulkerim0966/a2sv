class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dect={}
        for i in range(len(intervals)):
            dect[intervals[i][0]]=i
        temp=sorted(intervals)
        n=len(intervals)-1
        ans=[-1]*(n+1)
     
        for i in range(len(intervals)):
            j=0
            k=n
            end=intervals[i][1]
            while j<=k:
                mid=(j+k)//2
  
                if temp[mid][0]<end:
                    j=mid+1
                elif temp[mid][0]>=end:
                    k=mid-1
            if j <(n+1):
        
                ans[i]=dect[temp[j][0]]
        return ans
            

        
        
        