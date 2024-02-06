class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        su=0
        i=0
        while i<len(nums):
            su+=nums[i]
            i+=2
        return su
        