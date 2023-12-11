class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        ma=0
        if len(nums)==0:
            return 0
        count=1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]: 
                count+=1
                print(count)
            elif nums[i]!=nums[i+1]:
                ma=max(ma,count)
                count=1
        ma=max(ma,count)
        return ma
        
