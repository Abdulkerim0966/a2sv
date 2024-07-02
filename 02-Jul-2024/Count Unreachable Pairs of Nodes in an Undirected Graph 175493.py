# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        size = [1] * (n+1)
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
    
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    parent[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    parent[rootX] = rootY
                    size[rootY] += size[rootX]
     
        for x,y in edges:
            union(x,y)
        ans =0
        temp = set()
        for i in range(n):
            temp.add(find(i))

        for pr in temp:
            n-=size[pr]   
            ans +=(size[pr]*n)   
        return ans










        