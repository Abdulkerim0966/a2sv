class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        nr,nc = (len(matrix) , len(matrix[0]))
        count=0

        for r in range(nr):
            for c in range(1,nc):
                matrix[r][c] +=  matrix [r][c-1] 

        for c1 in range(nc):
            for c2 in range(c1,nc):

                dect={0:1}
                pre_su_ro=0

                for r in range(nr):

                    pre_su_ro += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                    count += dect.get (pre_su_ro - target ,0)
                    
                    dect[pre_su_ro] = dect.get(pre_su_ro , 0) + 1
        return count



