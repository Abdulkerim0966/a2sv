class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid (tup,r,c):
            row=len(board)
            col=len(board[0])
            if tup==(1,0) :
                return True if r+1 < row else False
            elif tup==(-1,0) :
                return True if r-1 >=0 else False
            elif tup==(0,1) :
                return True if c+1 < col else False
            elif tup==(0,-1) :
                return True if c-1 >=0 else False

        move=[(1,0),(0,1),(-1,0),(0,-1)]


                
        visited=set()

        def backtrack(r,c,i):
            
            if i>=len(word):
                return True  

            for j in move:
                if valid(j,r,c):
                    
                    if board[r+j[0]][c+j[1]] == word[i] and (r+j[0],c+j[1]) not in visited:
                        visited.add((r+j[0],c+j[1]))
                        if backtrack(r+j[0],c+j[1],i+1):
                            return True
                        visited.discard((r+j[0],c+j[1]))
      

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==word[0]:
                    visited.add((r,c))
                    if backtrack(r,c,1):
                        return True
                    visited.discard((r,c))

      