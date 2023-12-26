class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=max(heights)
        arr=[0]*(n+1)
        ans=[]
        
        for i in range(len(heights)):
            arr[heights[i]]+=1
        for i in range(len(arr)):
            for j in range(arr[i]):
                ans.append(names[heights.index(i)])
        ans.reverse()
        return ans 
       


        