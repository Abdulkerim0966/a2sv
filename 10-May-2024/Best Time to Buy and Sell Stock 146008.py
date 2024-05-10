# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        ma = prices[len(prices)-1]
        for i in range(len(prices)-1,-1,-1):
            prof =max(prof,ma -prices[i])
            ma =max(ma,prices[i])
        return prof