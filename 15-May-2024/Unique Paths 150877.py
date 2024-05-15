# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        direction={(0,1),(1,0)}
        def inbound(r,c):
            return (0 <= r <m and  0 <= c <n) 
        memo =defaultdict(int)
        def dp(r,c):
            # print(r,c)
            if r ==m-1 and c==n-1:
                return 1
            for i,j in direction:
                newrow = r+i
                newcol =c +j
                if inbound(newrow,newcol) :
                    # print(newrow,newcol)
                    if (newrow,newcol) not in memo:
                        memo[(newrow,newcol)] += dp(newrow,newcol)
                    memo[(r,c)] += memo[(newrow,newcol)]
            return memo[(r,c)]
        return dp(0,0)
        

        

        