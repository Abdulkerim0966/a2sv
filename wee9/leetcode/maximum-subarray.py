class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        ps=[0]
        for i in range(1,n+1):
            ps.append(ps[i-1]+nums[i-1])
        ma=float('-inf')
        left=0
        for i in range(1,n+1):
            if (ps[i]-ps[left])>ma:
                ma=(ps[i]-ps[left])
          
            while left<=i and (ps[i]-ps[left])<0:
                if (ps[i]-ps[left])>ma:
                    ma=(ps[i]-ps[left])
                left+=1
        return ma
            