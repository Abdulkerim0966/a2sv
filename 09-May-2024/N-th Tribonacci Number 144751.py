# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:

    def tribonacci(self, n: int) -> int:
        @cache
        def dfs(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            if num == 2:
                return 1
            
            return dfs(num-1) + dfs(num-2) + dfs(num-3)
        return dfs(n)

        