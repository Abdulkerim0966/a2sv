# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        l = sum(rolls)
        m =len(rolls)
        x =(mean*(m+n))-l
        print(l,m,x)
        if x >(n*6) or x<n:
            return []
        no = x//n
        ans =[no]*n
        t =x%n
        i =0
        while t>0:
            ans[i%n]+=1
            t-=1
            i+=1
        return ans


        