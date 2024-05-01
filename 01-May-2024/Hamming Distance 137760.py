# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x)[2:]
        b = bin(y)[2:]
        i=-1
        ans =0
        while abs(i)<= len(a) and abs(i)<= len(b):
            if a[i] != b[i]:
                ans +=1
            i-=1
        # print(i,a,b)
        if abs(i)<= len(a):
            # print(a[:i],a[i::-1])
            ans += a[:i+1].count('1')
        else:
            # print(b[:i],b[i::-1])
            ans += b[:i+1].count('1')
        return ans

        