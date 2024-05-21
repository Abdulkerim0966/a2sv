# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for r in range(len(triangle)-1,0,-1):
            for c in range(1,len(triangle[r])):
                triangle[r-1][c-1]+= min(triangle[r][c],triangle[r][c-1])
        return triangle[0][0]

        