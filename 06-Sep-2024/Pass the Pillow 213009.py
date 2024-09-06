# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        K = time % ((n*2)-2)
        if K < n :
            print(K,'hear')
            return K+1
        else:
            return (((n*2)-2)-K) + 1
        
        