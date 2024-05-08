# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        pre =[]
        pre.append(nums[0])
        ans = []
        for i in range(1,len(nums)):
            pre.append(pre[i-1]^nums[i])
        # print(pre)
        for i in range(len(pre)-1,-1,-1):
            # print(pre[i])
            temp = bin(pre[i])[2:]
            k =maximumBit
            poin =len(temp)-1
            temp2 = []
            while k>0 and poin >-1:
                # print(temp[poin])
                temp2.append('1' if temp[poin] == '0' else '0' )
                poin-=1
                k -=1
            while k>0:
                temp2.append('1')
                k-=1
            temp2.reverse()
            # print(temp2)
            ans.append(int(''.join(temp2),2))
        return ans


        