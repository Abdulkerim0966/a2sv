# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(i,s):
            if i ==len(prices):
                return 0
            
            if (i,s) not in memo:
                if s:
                    left = (prices[i]-fee) + dp(i+1,0)
                    right = dp(i+1,s)
                    memo[(i,s)]=max(left,right)
                else:
                    left=(-prices[i])+dp(i+1,1)
                    right = dp(i+1,s)
                    memo[(i,s)] =max(left,right)
            return memo[(i,s)]
        return dp(0,0)

            