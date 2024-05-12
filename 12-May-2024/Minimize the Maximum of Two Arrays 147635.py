# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:

        right =10**10
        left = 1
        target = uniqueCnt1 +uniqueCnt2
        g = abs(divisor1 * divisor2) // gcd(divisor1, divisor2)
        while left <= right:
            mid = (left+right)//2
            di1 = mid//divisor1
            di2 = mid//divisor2
            u = mid//g 
            # print(left,right,mid,di1,di2,u,g)
            if (mid-di1) >=uniqueCnt1 and mid-di2 >=uniqueCnt2 and mid -u >=target :
                right = mid -1
            else:
                left=mid+1
        # print(left,right)
        return left
        




















        # di1=0
        # di2 =0
        # u =0
        
        # s =1
        # while u +di1 +di2 < uniqueCnt1 +uniqueCnt2:
        #     if s%divisor1 !=0 and s%divisor2 !=0:
        #         u+=1
        #         s+=1
        #     elif  s%divisor1 !=0 and di1<uniqueCnt1:
        #         di1 +=1
        #         s +=1
        #     elif s%divisor2 !=0 and di2<uniqueCnt2:
        #         di2 +=1
        #         s +=1
        #     else:
        #         s+=1
        #     print(s,di1,di2,u)
        return s-1



        