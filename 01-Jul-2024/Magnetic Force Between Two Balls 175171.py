# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        right =max(position) - min(position)
        left = 1
        position.sort()

        def checker(n):
            t =1
            pre= position[0]
            i =1
            while i<len(position):
                if position [i]-pre>= n:
                    t+=1
                    pre =position [i]
                if t==m:
                    return True
                i+=1

        while left<=right:
            mid = (left+right)//2
            if checker(mid):
                left = mid+1
            else:
                right = mid-1
        return right
        