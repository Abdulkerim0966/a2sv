class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cheker(mid):
            count=0
        
            for i in range(len(piles)):
                count+=(ceil(piles[i]/mid))
                if count>h:
                    return False
            return True

        maxi=max(piles)
        mini=1

        while mini<=maxi:
            mid=(mini+maxi)//2
            temp = cheker(mid)
            if temp:
                maxi=mid-1
            if not temp:
                mini=mid+1
        return mini

        