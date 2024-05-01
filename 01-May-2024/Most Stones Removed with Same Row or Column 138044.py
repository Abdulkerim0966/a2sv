# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n =len(stones)
        
        root = [i for i in range(len(stones))]
        
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
    
        def union(x, y):
            nonlocal ans
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if root[rootX] <= root[rootY]:
                    root[rootY] = rootX
                    
                else:
                    root[rootX] = rootY
           
                ans +=1 
              
        ans =0
        for i in range( len(stones)):
            for j in range(1,len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
             
        return ans


        