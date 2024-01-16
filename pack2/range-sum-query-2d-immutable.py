class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.grid=[]
        t=[0]*(len(matrix[0])+1)
        self.grid.append(t)
        for r in range(len(matrix)):
            temp=[0]
            temp2=0
            for c in range(len(matrix[0])):
                temp2+=matrix[r][c]
                temp.append(temp2)
            self.grid.append(temp)
        # print(self.grid) 
        for c in range(len(matrix[0])+1):
            temp2=0
            for r in range(len(matrix)+1):
                temp2+=self.grid[r][c]
                self.grid[r][c]=temp2
        print(self.grid)



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return(self.grid[row2+1][col2+1]-self.grid[row2+1][col1]-self.grid[row1][col2+1]+self.grid[row1][col1])

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)