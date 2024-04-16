# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D



from heapq import heapify, heappop, heappush
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
    a = linp()
    for i in range(n):
        a[i] = (-a[i],i+1)
    
    heapify(a)
    temp = []
    ma = 0
    # print(a)
    while a:
        
        x = heappop(a)
        if a:
            y = heappop(a)
            if x[0] <0 and y[0] <0:
                x= (x[0]+1,x[1])
                ma +=1
                y= (y[0]+1,y[1])
                temp.append((x[1],y[1]))
            if  x[0] <0:
                heappush(a,(x[0],x[1]))
            if  y[0] <0:
                heappush(a,(y[0],y[1]))
            
           
            
        
            
    print(ma)
    for j in (temp):
        print(j[0],j[1])
        

        
    
    
    
 
q = iinp()
# q = 1
for _ in range(q):
    solve()