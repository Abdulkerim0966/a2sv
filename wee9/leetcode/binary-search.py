class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        while left+1<right:
            mid=(left+right)//2
            if nums[left]==target:
                return left
            elif nums[right]==target:
                return right
            elif nums[mid]>target:
                right=mid
            elif nums[mid]<target:
                left=mid
            elif nums[mid]==target :
                return mid
        return -1
            
        