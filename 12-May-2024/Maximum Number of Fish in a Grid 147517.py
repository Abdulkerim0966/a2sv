# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n =len(grid[0])
        direction={(0,1),(0,-1),(1,0),(-1,0)}
        def inbound(r,c):
            return (0 <= r <len(grid) and  0 <= c <len(grid[0]))
        root =[i for i in range(n*m)]
        def find (x):
            while x != root[x]:
                root[x] =root[root[x]]
                x = root[x]
            return x

        def union(x,y):
            parentx = find(x)
            parenty = find(y)

            if parentx != parenty:
                if parentx < parenty:
                    root[parenty] = parentx
                else:
                    root[parentx] = parenty

        visited = set()
        que = deque()
        for r in range (len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    que.append((r,c))
                    
        while que:
            # print(que)
            # t =len(que)
            temp = que.popleft()
            visited.add((temp[0],temp[1]))
            for i,j in direction:
                newrow = temp[0]+i
                newcol =temp[1] +j
                if inbound(newrow,newcol) and grid[newrow][newcol] >0:
                    # print(temp[0]*n+temp[1],newrow*n+newcol,newrow,newcol)
                    union (temp[0]*n+temp[1],newrow*n+newcol)
                    if (newrow,newcol) not in visited  :
                        que.append((newrow,newcol))
                        visited.add((newrow,newcol))

        ans =defaultdict(int)
        for r in range (len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    ans[find(r*n +c)]+=grid[r][c]
        # print(root,ans)
        ma=0
        for i in ans:
            ma =max(ans[i],ma)
        return ma

        
























        