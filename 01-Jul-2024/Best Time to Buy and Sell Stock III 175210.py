# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        H0= -math.inf
        H1 = -math.inf
        H2= -math.inf
        K1 = 0
        K2 =0
        K0 = 0
        

        for stock_price in prices:

            K1 = max(K1, H1 + stock_price)

            H1 = max(H1,  K0 - stock_price)

            K2 = max(K2, H2+ stock_price)

            H2 = max(H2, K1 - stock_price)

        return K2












        