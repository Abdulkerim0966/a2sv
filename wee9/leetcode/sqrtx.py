class Solution:
    def mySqrt(self, x: int) -> int:
        maxi=x
        mini=0

        while mini<=maxi:
            mid=(mini+maxi)//2
            now=mid*mid
            if now>x:
                maxi=mid-1
            elif now<x:
                mini=mid+1
            else:
                return mid
        return mini-1

        