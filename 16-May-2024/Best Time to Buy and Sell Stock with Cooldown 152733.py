# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(n,s):
   
            if n>= len(prices):
                return 0
            
            if (n,s) not in memo:
                if s:
                    left = prices[n] + (dp(n+2,0) if n+2<len(prices) else 0)
                    right =(dp(n+1,s) if n+1<len(prices) else 0)

                    memo[(n,s)] = max(left,right)
                else :
                    left =-prices[n] + (dp(n+1,1) if n+1<len(prices) else 0)
                    right = (dp(n+1,s) if n+1<len(prices) else 0)
                    memo[(n,s)] =max(left,right)
            return memo[(n,s)]

        return (dp(0,0))

        