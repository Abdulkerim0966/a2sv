class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[1]))
        x=float('-inf')
        ans=0
       
        for i in range(len(points)):
            if points[i][0]>x:
                ans+=1
                x=points[i][1]
        return ans


        