class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        re=True
        r=n
        while r!=0 and r!=1:

            if r%3!=0 and r%3!=1:
                re=False 
                break
            else:
                r=r//3
            
        return re
        