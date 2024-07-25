# Problem: D - The Kittens Test - https://codeforces.com/gym/520688/problem/D



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
    n = iinp()
    root = [i for i in range(n)]
    ans =[[i] for i in range(n)]
            
    def find(x):
        while x != root[x]:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def union(x, y):
        
        rootX = find(x-1)
        rootY = find(y-1)
        if rootX != rootY:
            if root[rootX] < root[rootY]:
                root[rootY] = rootX
                ans[rootX].extend(ans[rootY])
                
            else:
                root[rootX] = rootY
                ans[rootY].extend(ans[rootX])
                
   
    for  i in range(n-1):
        x,y =linp()
        union(x,y)
    temp =[]
    for item in ans:
        if len(item) ==n:
            return [i+1 for i in item]
            
          
    
    
 
# q = iinp()
q = 1
for _ in range(q):
    print(*solve())