class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        su=0
        sul=[]
        for i in range(len(nums)):
            su+=nums[i]
            sul.append(su)
        dect=Counter()
        ans=0
        for i in range(len(nums)):
            if sul[i]%k==0:
                ans+=1
            if sul[i]%k in dect:
                ans+=dect[sul[i]% k]
            dect[sul[i]%k]+=1
        return ans
        