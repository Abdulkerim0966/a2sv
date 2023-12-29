class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        longest=max(nums)
        mul=len(str(longest))

        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                order1 = int(str(nums[j]) + str(nums[j+1]))
                order2 = int(str(nums[j+1]) + str(nums[j]))
                if order2 > order1:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
                

        ans=list(map(str,nums))
        return str(int("".join(ans)))