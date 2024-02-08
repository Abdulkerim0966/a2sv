class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(len(grid)):
            grid[i].sort()
        for i in range(len(grid[0])):
            temp=[]
            for j in range(len(grid)):
                temp.append(grid[j][i])
            ans+=(max(temp))
        return ans

        