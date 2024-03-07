class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        col=len(matrix[0])
        initial=0
        final=(len(matrix)*len(matrix[0]))-1
        print(initial,final)
        while initial<=final:
            mid=(initial+final)//2
            r=mid//col
            c=mid%col
            if matrix[r][c]>target:
                final=mid-1
            elif matrix[r][c]==target:
                return True 
            else:
                initial=mid+1
        return  False

        
        