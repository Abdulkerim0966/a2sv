# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ma= max(nums)
        temp =0
        ans =1
        for i in range(len(nums)):
            if nums[i] ==ma:
                temp+=1
            else:
                temp =0
            ans =max(ans,temp)
        return ans



        