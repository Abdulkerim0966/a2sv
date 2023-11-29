class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        re=1
        while True:
            if re%2==0 and re%n==0:
                break
            else:
                re+=1
        return re

        