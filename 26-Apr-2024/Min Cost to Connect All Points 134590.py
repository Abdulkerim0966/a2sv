# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []
        for i in  range(len(points)):
            for j in range(i+1,len(points)):
                dis = abs(points[j][0]- points[i][0]) +abs(points[j][1]- points[i][1])
                edges.append((dis,i,j))
        
        # print(edges)
        edges.sort()
        root = [i for i in range(len(points))]
        
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
    
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if root[rootX] > root[rootY]:
                    root[rootY] = rootX
                    
                else:
                    root[rootX] = rootY
                    
                return True
            else:
                return False
        ans =0
        for pr ,x,y in edges:
            if  union(x,y):
                ans += pr
        return ans



        
        


        