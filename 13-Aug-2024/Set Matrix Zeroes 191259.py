# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        tober =set()
        tobecol =set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
               
                if matrix[r][c] ==0:
              
                    tober.add(r)
                    tobecol.add(c)
    
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in tober or c in tobecol:
                    matrix[r][c] =0
        
                    
        



        """
        Do not return anything, modify matrix in-place instead.
        """
        