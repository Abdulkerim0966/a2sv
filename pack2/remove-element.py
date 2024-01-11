class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right=len(nums)-1
        count=0
        for i in range(len(nums)):
            if nums[i]==val:
                while nums[right]==val and i<right:
                    right-=1
                nums[i],nums[right]=nums[right],nums[i]
                # count+=1
            if nums[i]!=val:
                count+=1
        print(count)
        return count
            

        