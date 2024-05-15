# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo =defaultdict(int)
        t =0
        def dp(n,t):
          
            
            if n==0:
                return 1
            if n<0:
                return 0
            if (n, t) not in memo:

                for i in range(t,len(coins)): 
                    if coins[i]<=n:
                        memo[(n, t)] +=dp(n-coins[i],i)
                   
                
            return memo[(n, t)]
        ans = dp(amount,0)

        return ans 
        