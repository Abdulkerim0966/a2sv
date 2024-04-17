# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(mat) and 0 <= col < len(mat[0]))

        que =deque() 
        row = len(mat)
        col =len(mat[0])
        ans =[]
        visited =set()
        for r in range(row):
            temp =[]
            for c in range(col):  
                if mat[r][c] == 0:
               
                    que.append((r,c))
                    visited.add((r,c))
                temp.append(0)
            ans.append(temp)
       
        count = 0
        while que:
            len(que)
            
            for i in range(len(que)):
                row , col = que.popleft()
           
                if mat[row][col] == 1:
                    if ans[row][col] == 0:
                        ans[row][col] = count
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    if inbound(new_row,new_col) and (new_row,new_col) not in visited:
                        visited.add((new_row,new_col))
                        que.append((new_row,new_col))
            
            count += 1

     
        return ans

          

            

