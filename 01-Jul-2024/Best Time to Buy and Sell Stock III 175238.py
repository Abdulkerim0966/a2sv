# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1,s1,b2,s2 =-prices[0],0,-prices[0],0
        
        for p in prices:
            b1 = max(b1,-p)
            s1 = max (s1,b1+p)
            b2 = max(b2,s1-p)
            s2 = max(s2,b2+p)
        return s2














        