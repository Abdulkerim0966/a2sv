class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        i=0
        while j<len(nums):
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                j+=1
            else:
                i+=1
                j+=1


   
        