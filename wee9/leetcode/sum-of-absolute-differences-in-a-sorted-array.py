class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre=[]
        pre.append(nums[0])
        for i in range(1,len(nums)):
            pre.append(pre[i-1]+nums[i])

        total=pre[-1]
        for i in range(len(nums)):
            nums[i]=(((nums[i]*i)-(pre[i]-nums[i]))+((total-pre[i])-(nums[i]*(len(nums)-(i+1)))))
        return nums