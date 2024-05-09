# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ans ={i for i in range(n)}
        for x,y in edges:
            ans.discard(y)
        if len(ans)>1:
            return -1
        else:
            for i in ans:
                return i
        
          