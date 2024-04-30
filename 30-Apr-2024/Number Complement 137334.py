# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        
        temp = bin(num)[2:]
        n=len(temp)
        t = (1<<(n))-1
   
        return num ^ t
        