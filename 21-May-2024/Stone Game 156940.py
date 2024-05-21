# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo ={}
        total =sum(piles)
        def  dp(i,j):
            if i == j:
                return 0
            
            if (i,j) not in memo:
                left = piles[i]+ dp(i+1,j)
                right =piles[j] +dp(i,j-1)
                memo[(i,j)] = max(left,right)
            return memo[(i,j)]
        return dp(0,len(piles)-1) > total/2

        