# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def inbound(r,c):
            return 0 <= r<n and 0 <= c< m
        
        direction =[(0,1),(1,0),(-1,0),(0,-1)]

        visited =set()
        def bfs(iland,r,c):
            nonlocal visited
            iland.append((r,c))
            visited.add((r,c))

            for i,j in direction:
                newr = r+i
                newc = c+j
                if inbound(newr,newc) and (newr,newc) not in visited and grid2[newr][newc] ==1:
                    bfs(iland,newr,newc)
            return iland



        n =len(grid1)
        m =len(grid1[0])
        land= []
        for r in range(n):
            for c in range(m):
                if grid2[r][c] ==1:
                    land.append((r,c))
        ans =[]
        for r,c in land:
            if (r,c) not in visited:
                ans.append(bfs([],r,c).copy())
        temp =0
        for iland in ans:
            
            for r,c in iland:
                if grid1[r][c] ==0:
                    break
            else :
                temp+=1
        return temp





        

