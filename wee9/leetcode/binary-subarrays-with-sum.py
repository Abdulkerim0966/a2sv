class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dect=Counter()
        ans=0
        ps=[]
        ps.append(0)
        for i in range(len(nums)):
            ps.append(ps[i]+nums[i])
        for i in range(1,len(nums)+1):
            if ps[i]==goal:
                ans+=1
                
            
            if (ps[i]-goal) in dect:
                ans+=dect[(ps[i]-goal)]
            dect[ps[i]]+=1
        return ans
                