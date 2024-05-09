# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        if  n&2 == 1:
            return False
        n /= 2
        @cache
        def dp(i,target):
            if target ==0:
                return True
            if i == len(nums) :
                return False
            if target < 0:
                return False

            return dp(i+1,target -nums[i]) or dp(i+1,target)
        
        return dp(0,n)
            
        