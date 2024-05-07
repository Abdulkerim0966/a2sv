# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        a= bin(left)[2:]
        b = bin(right)[2:]
        n = max(len(a),len(b))
        # print(a,b)
        temp=[0]*n
        s=0
        for i in range(len(a)-1,-1,-1):
            temp[n-s-1] = int(a[i])
            s+=1

        temp2 =[0]*n
        s=0
        for i in range(len(b)-1,-1,-1):
            temp2[n-1-s] = int(b[i])
            s+=1
        ans =0

        # print(temp,temp2)
        for i in range(n):
            if temp[i]^temp2[i] == 1:
                break
            elif temp[i] &temp2[i] ==1:
                ans+=(2**(n-1-i))
        return ans



        