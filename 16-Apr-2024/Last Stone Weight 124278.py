# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range (len(stones)):
            stones[i] =( - stones[i]) 
        heapify(stones)
        while len(stones) >1:
            x = -heappop(stones)
            y = -heappop(stones)
            x-=y
            if x!=0:
                heappush(stones,-x)
        

        return -stones[-1] if stones else 0

        