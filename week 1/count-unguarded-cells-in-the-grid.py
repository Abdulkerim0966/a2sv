class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        grid=[[0]*n for item in range(m)]

        for i in range(len(walls)):
            grid[walls[i][0]][walls[i][1]]=1

        for i in range(len(guards)):
            grid[guards[i][0]][guards[i][1]]='G'
        # print (grid)
        for i in range(len(guards)):
            


            for up in range(guards[i][0]-1,-1,-1):
                if grid [up][guards[i][1]]==1:
                    break
                elif grid [up][guards[i][1]]=='G':
                    break
                else:
                    grid[up][guards[i][1]]='g'

            for dawn in range(guards[i][0]+1,m,):
                if grid [dawn][guards[i][1]]==1:
                    break
                elif grid [dawn][guards[i][1]]=='G':
                    break
                
                else:
                    grid[dawn][guards[i][1]]='g'


            for right in range(guards[i][1]-1,-1,-1):
                if grid [guards[i][0]] [right]==1:
                    break
                elif grid [guards[i][0]] [right]=='G':
                    break
                else:
                    grid [guards[i][0]] [right]='g'

            for left in range(guards[i][1]+1,n):
                if grid [guards[i][0]] [left]==1:
                    break
                elif grid [guards[i][0]] [left]=='G':
                    break
                else:
                    grid [guards[i][0]] [left]='g'
        count=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    count+=1
        # print (grid)
        return count


            



        