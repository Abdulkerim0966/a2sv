# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
     
        dect={}

        def cal(sum):
            
            if sum in dect :
                return dect[sum]
            if sum == 1 or sum == 0 :
                return 1

            result = cal (sum -1) + cal(sum -2)

            dect[sum] = result
            return result
        
        
        return cal(n)
                
            
            
        