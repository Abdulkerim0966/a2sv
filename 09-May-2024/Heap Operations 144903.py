# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C



from heapq import heappop, heappush
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
    hea =[]
    ans = []
    for _ in range(n):
        a = string()
        if a[0] == 'i':
            ans.append(a)
          
            temp =-(int(a[8:]))if a[7] =='-' else int(a[7:])
            heappush(hea,temp)
        elif a[0] == 'r':
            if hea:
                ans.append(a)
                heappop(hea)
            else:
                ans.append('insert '+'1')
                ans.append(a)
        else:
            temp =-(int(a[8:]))if a[7] =='-' else int(a[7:])
            if not hea or temp <hea[0]:
                ans.append('insert '+str(temp) )
                ans.append(a)
                heappush(hea,temp)
                
            elif temp == hea[0]:
                ans.append(a)
            else:
                while hea and temp > hea[0]:
                    ans.append('removeMin')
                    heappop(hea)
                if not hea or temp < hea[0]:
                    ans.append('insert '+str(temp) )
                    ans.append(a)
                    heappush(hea,temp)
                else:
                    ans.append(a)
    print(len(ans))
    for i in ans:
        print (i)
    
 
# q = iinp()
q = 1
for _ in range(q):
    solve()