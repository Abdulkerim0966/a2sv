# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo ={}
        def dp(n):
            if n==0:
                return 1
       
            if n not in memo:
                ans=n
                for i in range(1,n):
                    if n-i>=0:
                        ans = max(ans,i*dp(n-i))
                memo[n] = ans
            return memo[n]
        if n ==2:
            return 1
        if n==3:
            return 2
        ans = dp(n)
    
        return ans 


        