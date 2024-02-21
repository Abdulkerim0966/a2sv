class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        mo=0
        while maxDoubles >0 and target > 1:
            if target%2==1:
                mo+=1
                target-=1
            else:
                mo+=1
                target //=2
                maxDoubles-=1
        if target>1:
            mo+=(target-1)
        return mo
        