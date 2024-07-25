# Problem: Maximum Number of Zeros - https://codeforces.com/gym/514644/problem/D



from re import M
import sys
from tokenize import Double
 
 
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
from math import ceil, gcd
 
 
def solve():
    
    n=iinp()
    a = linp()
    b = linp()
    dect = Counter()
    ans=[]
    count=0
    for i in range(n):
        if a[i] == 0 and b[i]!=0:
            continue
        else:
            if a[i] == 0 and b[i] == 0:
                count+=1
            else:
                x=gcd(a[i],b[i])
                ai=a[i]/x
                bi=b[i]/x
                if ai*bi >=0:
                    ans.append((-abs(ai),abs(bi)))
                else:
                    ans.append((abs(ai),abs(bi)))
    dect=Counter(ans)
    if len(dect) ==0 :
        print(0+count)
    else:
        print(max(dect.values()) +count)

# q = iinp()
q = 1
for _ in range(q):
    solve()