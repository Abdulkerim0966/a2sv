class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)-1
        while n>0:
            for i in range(n):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]

                    
            n-=1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        