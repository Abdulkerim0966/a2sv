# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int) 
        ma = 0
        for i in range(len(arr)-1,-1,-1):
            memo[arr[i]] = memo[arr[i]+difference]+1
            ma =max(ma,memo[arr[i]])
        return ma
