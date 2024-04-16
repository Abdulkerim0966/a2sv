# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        
        heapify(piles)
        for i in range(k):
            temp =-heappop(piles)
      
            temp -= (temp//2)

            heappush(piles,-temp)
            


         
        return -sum(piles)