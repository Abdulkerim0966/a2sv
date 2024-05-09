# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B



from gc import get_count
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
    n, m,k = linp()
 
    ar =[]
    for i in range(m+1):
        ar.append(iinp())
    ans =0
    for j in range(len(ar)-2,-1,-1):
        if bin(ar[m]^ar[j]).count('1') <=k:
            ans+=1
    print(ans)
    
 
# q = iinp()
q = 1
for _ in range(q):
    solve()