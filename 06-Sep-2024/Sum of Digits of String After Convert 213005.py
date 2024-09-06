# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp=""
        for ch in s:
            temp+= str((ord(ch)-96) )
        (print(temp))
        for i in range(0,k):
            s =str(temp)
            temp =0
            for ch in s:
                temp+= (int(ch)) 
            print(temp)
        return temp

        