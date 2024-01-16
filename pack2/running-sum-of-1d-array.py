class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=[]
        tsum=0
        for i in range (len(nums)):
            tsum+=nums[i]
            sum.append (tsum)
        return sum