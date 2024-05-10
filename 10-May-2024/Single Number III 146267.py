# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
       
        x = nums[0]
        for i in range(1,len(nums)):
            x ^=nums[i]
        y = x
        x = bin(x)
        s =-1
        while x[s] != '1':
            s-=1
       
        n1 = 0
        n2 = 0
        for i in range(len(nums)):
            # print((1 << (-s-1)),s,bin(y))
           
            if (1 << (-s-1)) &nums[i]:
                n1 ^= nums[i]
            else:
                n2 ^= nums[i]
        return [n1,n2]


        


        