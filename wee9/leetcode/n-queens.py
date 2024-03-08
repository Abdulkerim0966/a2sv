class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
    
        bucket=[]
        ans=[]
        col=set()
        ldia=set()
        rdia=set()
        
        
        def backtrack(r):
            
            if r == n:
        
                ans.append(bucket.copy())
                return
                
            for c in range(n):
                if (c not in col) and ((r + c) not in ldia) and ((r - c) not in rdia):
                    col.add(c)
                    ldia.add(c + r)
                    rdia.add(r - c)     
                    bucket.append((r, c))
                    backtrack(r+1)
                    bucket.pop()
                    col.discard(c)
                    ldia.discard(c + r)
                    rdia.discard(r - c)
        for c in range(n):
            col=set([c])
            ldia=set([c])
            rdia=set([-c])    
            bucket = [(0, c)]
            backtrack(1)
        
        # print(ans)
        temp=[]

       
        for i in range(len(ans)):
            board=[['.']*n for _ in range(n)]
         
            for j in range(len(ans[i])):
                board[ans[i][j][0]][ans[i][j][1]]='Q'
            
            temp.append(''.join(a) for a in board)

             
        return temp
            







        
       
       