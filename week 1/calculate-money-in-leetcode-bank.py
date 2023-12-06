class Solution:
    def totalMoney(self, n: int) -> int:
        count=0
        mo=0
        no_w=ceil(n/7)
        for i in range (1,no_w+1):
            for j in range(7):
                if count==n:
                    break
                else:
                    mo+=(i+j)
                    count+=1
        return mo
