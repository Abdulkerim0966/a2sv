class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
     

        left=0
        right=len(nums)-1
        ans=[-1,-1]
        while left<right :
            mid=(left+right)//2
            
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>=target:
                right=mid 
        
     
        if not nums  or nums[left]!=target:
            return [-1,-1]
        ans[0]=left

        left=0
        right=len(nums) -1  
        
        while left<=right :
       
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
               left=mid+1
            else:
                ans[1]=mid
                left=mid+1


            
        return ans
            
        