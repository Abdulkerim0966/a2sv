class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        ma=0
        for i in range(len(points)-1):
            if ma<(points[i+1][0]-points[i][0]):
                ma=(points[i+1][0]-points[i][0])
        return ma