# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D



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
    n= iinp()
    a = linp()
    dect = defaultdict(int)
    def factor(n):
        d=2
        while d  * d <= n :
          
            while n%d == 0:
                dect[d]+=1
                n //=d
            
            d+=1
        if n !=1:
            dect[n] +=1
    for num in a:
        factor(num)
    for i in dect:
        if dect[i] %n !=0:
            print('NO')
            break
    else:
        print('YES')
q = iinp()
# q = 1
for _ in range(q):
    solve()