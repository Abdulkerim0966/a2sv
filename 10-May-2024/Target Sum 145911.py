# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans =0
        @cache
        def dp(i ,su):

           
            if i == len(nums):
                # print('hrer',su,i)
                if su == target:
                   return  1
                else:
                    return 0
             
            
            
            return dp(i+1,su+nums[i]) + dp(i+1,su-nums[i])

        return dp(0,0)
        



        