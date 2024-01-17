class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum=[]
        tsum=0
        sum.append (0)
        for i in range (len(nums)):
            tsum+=nums[i]
            sum.append(tsum)
        re=-1
        for i in range (len(nums)):
            if sum[i]==(sum[len(nums)]-sum[i+1]):
                re= i
                break
            else :continue
        return re

        