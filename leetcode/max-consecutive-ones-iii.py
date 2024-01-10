class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ma=0
        left=0
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            while count>k:

                if nums[left]==0:
                    count-=1
                left+=1
            ma=max(ma,i-left+1)
        
        return ma
        
        