class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        left_right=set( i for i in range(left,right+1))
        for i in range(len(ranges)):
            for i in range(ranges[i][0],ranges[i][1]+1):
                left_right.discard(i)
        if len(left_right)==0:
            return True

           
        return False