class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pl=[1]
        for i in range(len(nums)):
            pl.append(pl[i]*nums[i])
        pr=[1]*(len(nums)+1)
        for i in range(len(nums)-1,-1,-1):
            pr[i]=(pr[i+1]*nums[i])
        ans=[1]*(len(nums))
        # print(pl,pr)
        for i in range(len(nums)):
            ans[i]=(pl[i]*pr[i+1])

        return ans


        