# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo ={}
        def dp(n):
            if n==0:
                return 0
            if n<0:
                return float('inf')
            if n not in memo:
                ans=float('inf')
                for i in coins:
                    ans = min(ans,dp(n-i))
                memo[n] = ans
            return memo[n]+1
        ans = dp(amount)
        return ans  if  ans!=float('inf') else -1



        
        