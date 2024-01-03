class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right=1
        left=0
        k=1
        while right<len(nums):
            if nums[left]>=nums[right]:
                right+=1
            elif right!=left+1:
                nums[left+1],nums[right]=nums[right],nums[left+1]
                left+=1
                k+=1
            else :
                k+=1
                left+=1
                right+=1
        return k
            


        