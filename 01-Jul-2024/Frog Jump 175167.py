# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        last = stones[-1]
        memo = {}
        stone = set(stones)
        def dp(t,j):
            print(t,j)
            if t == last:
                return True
            if t not in stone:
                return False
            if (t,j) not in memo :
                l = (dp(t+(j-1),j-1)) if  j > 1 else False
                r= dp(t+j,j) 
                m= dp(t+(j+1),j+1)
                memo[(t,j)] = l or r or m
            
            return memo[(t,j)] 
        
        return (dp(stones[1],1)) if stones[1]-1 == stones[0] else False
        



















