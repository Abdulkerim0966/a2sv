class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        x=nums[right]
      
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<x:
                right=mid-1
                x=nums[mid]
            else:
                left=mid+1
                
            
        return x