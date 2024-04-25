# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        root = [i for i in range(len(edges)+1)]
        size = [1] * (len(edges)+1)
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
 
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]
            else:
                return True
        for x,y in edges:
            if  union(x,y):
                return [x,y]


            
        


















