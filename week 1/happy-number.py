class Solution:
    def isHappy(self, n: int) -> bool:
        se=set()

        while n not in se:
            su=0
            se.add(n)
            while n>0:
                su+=(n%10)**2
                n//=10
            
            print(se)
            if su==1:
                return True
            n=su
        return False


        