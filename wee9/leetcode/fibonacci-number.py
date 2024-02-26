class Solution:
    def fib(self, n: int) -> int:
        def calculator(n:int):
            if n==0:
                return 0

            if n==1:
                return 1

            temp=(calculator(n-1)+calculator(n-2))
            return temp
        
        ans = calculator(n)

        return ans



        