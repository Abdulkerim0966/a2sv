class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n=len(mat)
        m=(n//2)
        count=0
        visited=set()
        for i in range(n):
            visited.add((i,i))
            count+=mat[i][i]
        for i in range(n):
            count+=mat[i][n-1-i]
        if n%2==1:
            count-=mat[m][m]
        return(count)