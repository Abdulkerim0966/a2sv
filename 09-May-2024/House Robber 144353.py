# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo ={}
        def dfs(n):
            if n == 0:
                return nums[n]
            if n ==1:
                return max(nums[0],nums[1])
            if n not in memo:
                memo[n] = max(dfs(n-1), dfs(n-2) + nums[n])
            return memo[n]
        return dfs(len(nums)-1)
       

        