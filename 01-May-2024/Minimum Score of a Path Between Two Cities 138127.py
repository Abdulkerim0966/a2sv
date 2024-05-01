# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        root=[i for i in range(n)]
        ans = [float('inf') for i in range(n)]
        def find(x):
            while root[x] != x:
                root[x] = root[root[x]]
                x =  root[x]
            return x
        def union(x,y,val):
            parentx =find(x)
            parenty = find(y)

            if parentx != parenty:
                if parentx <= parenty:
                    root[parenty] = parentx
                    ans[parentx] =min(ans[parentx] , val,ans[parenty])
                else:
                    root[parentx] = parenty
                    ans[parenty] =min(ans[parenty] , val,ans[parentx])
            else:
                ans[parentx] =min(ans[parentx] , val)

        for x,y,v  in roads:
            union(x-1,y-1,v)
        # print(ans)
        return ans[find(0)]
        
        