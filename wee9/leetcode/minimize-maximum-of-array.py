class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mi=nums[0]
        pres=nums[0]
        for i in range(1,len(nums)):
            pres+=nums[i]
            ava=ceil(pres/(i+1))
            mi=max(mi,ava)
        return mi
        


                
        
        