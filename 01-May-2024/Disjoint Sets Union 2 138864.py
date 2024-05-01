# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B



from heapq import heappush
from re import M
import sys
 
 
def iinp():
    return int(sys.stdin.readline().strip())
 
 
def linp():
    return list(map(int, sys.stdin.readline().strip().split()))
 
 
def lsinp():
    return sys.stdin.readline().strip().split()
 
 
def digit():
    return [int(i) for i in (list(sys.stdin.readline().strip()))]
 
 
def char():
    return list(sys.stdin.readline().strip())
 
 
def string():
    return sys.stdin.readline().strip()
 
 
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil
 
 
def solve():
    n, m = linp()
    maxi =[[i,1] for i in range(1,n+1)]
    
    
    root = [i for i in range(n)]
    
    def find(x):
        while x != root[x]:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if root[rootX] <= root[rootY]:

                if maxi[rootY][0] >maxi[rootX][0]:
                    maxi[rootX][0] = maxi[rootY][0] 
          
                root[rootY] = rootX
                
                maxi[rootX][1] += (maxi[rootY][1])
            else:
             
                if maxi[rootY][0] <maxi[rootX][0]:
                    maxi[rootY][0] = maxi[rootX][0] 
                 
                root[rootX] = rootY
                maxi[rootY][1] += (maxi[rootX][1])
                
    for _ in range(m):
        qu =lsinp()
        # print(qu)
        if qu[0] == 'union':
            union(int(qu[1])-1,(int(qu[2]))-1)

        else:
            x = find(int(qu[1])-1)
            print(x+1,maxi[x][0],maxi[x][1])
            
            
            
        
    
    
 
# q = iinp()
q = 1
for _ in range(q):
    solve()