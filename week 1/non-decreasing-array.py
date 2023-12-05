class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        f1=False
        ans=True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if f1==True:
                    ans=False
                else:
                    f1=True
                    if i==0 or nums[i-1]<=nums[i+1]:
                        continue
                    else :
                        nums[i+1]=nums[i]
        return ans
        