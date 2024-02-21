class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans=0
        rowMax=[]
        colMax=[0]*len(grid[0])
        for r in range(len(grid)):
            rowMax.append(max(grid[r]))
            for c in range(len(grid[0])):
                colMax[c]=max(colMax[c],grid[r][c])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ma=min(rowMax[r],colMax[c])
                ans+=(ma-grid[r][c])

        return ans


        