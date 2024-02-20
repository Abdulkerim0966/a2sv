class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        pes=[0]*(n+1)
        nums.sort()
        ans=0
        for i in range(len(requests)):
            pes[requests[i][0]]+=1
            pes[requests[i][1]+1]-=1
        for i in range(1,len(pes)):
            pes[i]=(pes[i-1]+pes[i])

        pes.sort()
        for i in range(len(nums)):
            ans+=(pes[i+1]*nums[i])
        return ans%1000000007
            
        