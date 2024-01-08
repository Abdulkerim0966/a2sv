class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        ma=(sum(nums[:k])/k)
        
        su=sum(nums[:k])
        
        for i in range(1,len(nums)-(k-1)):
      
            su=((su-nums[i-1])+nums[i+(k-1)])
            if ma<=(su)/k:

                ma=(su)/k
        return ma

        