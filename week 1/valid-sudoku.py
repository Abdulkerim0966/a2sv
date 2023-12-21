class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            co=set()
            ra=set()
            for j in range(9):
                if board[i][j] in co:
                    return False
                elif board[i][j]!='.':
                    co.add(board[i][j])
            for j in range(9):
                if board[j][i] in ra:
                    return False
                elif board[j][i]!='.':
                    ra.add(board[j][i])

        for i in range(0,9,+3):
            for j in range(0,9,+3):
                cu=set()
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c] in cu:
                            return False
                        elif board[r][c]!='.':
                            cu.add(board[r][c])


        
        return True


        