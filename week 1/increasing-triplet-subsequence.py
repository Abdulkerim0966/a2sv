class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        val=nums[0]
        val2=float('inf')
        for i in range(1,len(nums)):
            if nums[i]>val2:
                return True
            elif nums[i]<val:
                val=nums[i]
            elif nums[i]<val2 and nums[i-1]!=nums[i] and val!=nums[i]:
                val2=nums[i]
        return False

        
       

        