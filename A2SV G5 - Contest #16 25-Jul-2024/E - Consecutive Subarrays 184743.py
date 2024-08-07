# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E



from itertools import accumulate
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
    n, b = linp()
    a = linp()
    pre = list(accumulate(a[::-1]))[::-1]
    print(pre[0]  + sum(sorted(pre[1:])[::-1][:b-1]))
    
 
# q = iinp()
q = 1
for _ in range(q):
    solve()