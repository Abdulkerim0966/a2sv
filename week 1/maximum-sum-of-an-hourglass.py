class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        count=[]
        for i in range(len(grid[0])-2):
            for j in range(len(grid)-2):
                count.append(grid[j][i]+grid[j][1+i]+grid[j][2+i]+grid[1+j][1+i]+grid[2+j][i]+grid[2+j][1+i]+grid[2+j][2+i])
        
        return max(count)
                

       

        