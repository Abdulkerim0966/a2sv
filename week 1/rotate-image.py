import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        size=len(matrix)
        if size%2==0:
            n=size//2
            size -= 1
            for i in range(n):
                for j in range(n):
                    matrix[i][j],matrix[j][size-i],matrix[size-i][size-j],matrix[size-j][i]=matrix[size-j][i],matrix[i][j],matrix[j][size-i],matrix[size-i][size-j]
        else:
            n=size//2
            size -= 1
            for i in range(n+1):
                for j in range(n):
                    matrix[i][j],matrix[j][size-i],matrix[size-i][size-j],matrix[size-j][i]=matrix[size-j][i],matrix[i][j],matrix[j][size-i],matrix[size-i][size-j]
        



        


        



        """
        Do not return anything, modify matrix in-place instead.
        """
        