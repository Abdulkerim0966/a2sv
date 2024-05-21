# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m =len(obstacleGrid)
        n =len(obstacleGrid[0])
        memo =[[0]*n for _ in range(m)]
        if obstacleGrid[0][0] ==0:
            memo[0][0] = 1
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] ==0:
                    # print(r,c)
                    if r-1>=0:
                        memo[r][c] += memo[r-1][c]
                    if c-1 >= 0:
                        memo[r][c] += memo[r][c-1]
                    # print (memo[r][c])
            # print(memo)
        return memo[-1][-1]

        # def dp(r,c):
        #     if (r,c) == (m-1,n-1) and obstacleGrid[r][c] ==0:
        #         return 1
        
        #     if (r,c) not in memo:
        #         if obstacleGrid[r][c] == 1:
        #             memo[(r,c)] = 0
        #         else:
        #             left =dp(r,c+1) if c+1 < n else 0
        #             right =dp(r+1,c) if r+1 <m else 0
        #             memo[(r,c)] =left +right
        #     return memo[(r,c)]

        # return dp(0,0)

        