# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo ={}
        m =len(matrix)
        n = len(matrix[0])

        def dp(r,c):
            
            if (r,c) not in memo:
                right = (dp(r,c+1) if c+1 < n else 0)
                down = (dp(r+1,c) if r+1 <m else 0)
                dia = (dp(r+1,c+1) if r+1<m and c+1<n else 0)

                memo[(r,c)] = ((1+min(right,down,dia)) if matrix[r][c] == '1' else 0)
            return memo[(r,c)]
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    ans = max(ans,dp(r,c))
  
        return ans**2

        