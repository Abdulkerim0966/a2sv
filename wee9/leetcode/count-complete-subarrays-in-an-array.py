class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        SE=set(nums)
        n=len(SE)
        dect=Counter()
        ans=0
        for i in range(len(nums)):
            dect[nums[i]]+=1
            if len(dect)==n:
                ans+=1
            for j in range(i+1,len(nums)):
                dect[nums[j]]+=1
                if len(dect)==n:
                    ans+=1 
            dect.clear()
           
        return ans