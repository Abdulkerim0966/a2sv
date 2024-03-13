class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count=0
        ma=nums[-1]
        for i in range(len(nums)-1,-1,-1):
            temp2=count
            count+=(((nums[i]+(ma-1))//ma)-1)
            ma=nums[i]//((count+1)-temp2)
          
        return count
       