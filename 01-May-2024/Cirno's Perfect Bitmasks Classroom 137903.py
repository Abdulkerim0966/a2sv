# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A



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
    # n, b = linp()
    a = iinp()
    x= -1
    b=bin(a)[2:]
    n=len(b)
    x =b.rindex('1')
    # print(b,x,n,(n-x -1))
    
    if n == 1:
        return 3
        
    else:
        if b[-1] == '1':
            if b[-2] == 0:
                return 3
            else:
                return 1
        else:
            if b.count('1') ==1:
                return int(1<<(n-x -1) | 1)
            else:
                return int(1<<(n-x -1))
        
    
    
    
    
    
        
    
 
q = iinp()
# q = 1
for _ in range(q):
    print(solve())