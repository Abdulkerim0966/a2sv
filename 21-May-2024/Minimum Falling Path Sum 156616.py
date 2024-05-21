# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        memo ={}
        def dp(r,c):
            if r == n-1:

                return matrix[r][c]
            
            if (r,c) not in memo:
                # print(matrix[r][c])
                mid = matrix[r][c] + (dp(r+1,c))
                right = matrix[r][c] + (dp(r+1,c+1) if c+1 <n else float('inf'))
                left = matrix[r][c] + (dp(r+1,c-1) if c-1 >=0 else float('inf'))
                # print(mid,left,right)
                memo[(r,c)] = min(mid,left,right)
            # print(memo[(r,c)])
            return memo[(r,c)]

        # ans =dp(0,1)
        ans = float('inf')
        for i in range(n):
            ans =min(ans,dp(0,i))
            # print(dp(0,i))
        return ans


    
        