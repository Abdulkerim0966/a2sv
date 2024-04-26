# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x:x[2])
        pointer = 0
        for i in range(len(queries)):
            queries[i].append(i)

        queries.sort(key=lambda x:x[2])
        root = [i for i in range(n)]
        # print(queries)
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
    
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if root[rootX] < root[rootY]:
                    root[rootY] = root[rootX]
                    
                else:
                    root[rootX] = root[rootY]
              
        ans =[True]*len(queries)
        
        for x,y,li,idx in queries:

            while pointer < len(edgeList) and edgeList[pointer][2]<li:
                union(edgeList[pointer][0],edgeList[pointer][1])
                pointer +=1
            
            # print(root)
            ans[idx] = (find(x) == find(y))
                
        return ans

        