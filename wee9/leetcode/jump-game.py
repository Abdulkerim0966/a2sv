class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m=1
        for i in range(len(nums)-2,-1,-1):
            if m<=nums[i]:
                m=1
            else:
                m+=1
        return m==1


        