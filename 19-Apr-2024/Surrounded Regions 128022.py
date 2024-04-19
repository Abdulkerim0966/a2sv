# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(board) and 0 <= col < len(board[0]))


        def dfs(row,col,visited):
            visited.add((row,col))
            if board[row][col] == "X":
                return True
            ans = True
            for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    if not inbound(new_row,new_col) :
                        return False
                    if (new_row,new_col) not in visited and board[new_row][new_col] == "O" :
                        ans = (ans and dfs(new_row , new_col,visited))

            return ans

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    visited =set()
                    if dfs(r,c,visited):
                        for row , col in visited:
                            board[row][col] = "X"










