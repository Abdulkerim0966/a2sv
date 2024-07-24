# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        k, mini = len(nums) - 1, float("inf")
        if k + 1 < 5: return 0
        nums.sort()
        for i in range(4): mini = min(mini, nums[k + i - 3] - nums[i])
        return mini