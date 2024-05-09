# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def calculator(n:int):
            if n in memo :
                return memo[n]
            if n==0:
                return 0

            if n==1:
                return 1
            if n not in memo: 
                temp=(calculator(n-1)+calculator(n-2))
                memo[n] = temp
            return memo[n]
        
        ans = calculator(n)

        return ans



        