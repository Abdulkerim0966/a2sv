# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       
        arr =[0]*31
        arrn = [0]*32
        for num in nums:
            s=0
            bi = bin(num)
            if bi[0] == '-':
                bi = bi[3:]
                for i in range (len(bi)-1,-1,-1):
                    if bi[i]=='1':
                        arrn[s]+=1
                    s+=1

            else:
                bi = bi[2:]
                for i in range (len(bi)-1,-1,-1):
                    if bi[i]=='1':
                        arr[s]+=1
                    s+=1
        ans = 0
        for i in range(len(arr)):
            if arr[i]%3 != 0:
                ans +=(2**i)
        for i in range(len(arrn)):
            if arrn[i]%3 != 0:
                ans -=(2**i)
        return ans
        



        