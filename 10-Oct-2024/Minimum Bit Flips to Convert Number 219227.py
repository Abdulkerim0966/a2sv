# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a=bin(start)[2:]
        b =bin(goal)[2:]
        if len(a)>len(b):
            a,b =b,a
        n,m =len(a),len(b)
        ans =0
        i =-1
        while abs(i) <=n:
            if a[i] != b[i]:
                ans +=1
            i-=1
        while abs(i) <=m:
            if b[i] =="1":
                ans+=1
            i-=1
        return ans



        