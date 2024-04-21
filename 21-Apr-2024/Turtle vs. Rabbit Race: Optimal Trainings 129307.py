# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E



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
    for i in range(1,len(a)):
        a[i] +=(a[i-1])
    qu = iinp()
    ans =[]
    # print(a)
    for _ in range(qu):
        l,u = linp()
        left  =l-1
        right =len(a)-1
        
        while left <= right:
            mid = (left+right)//2
            # print (mid,a[mid]-(a[l-2] if  l!=1 else 0) , a[l-2])
            if a[mid]-(a[l-2] if  l!=1 else 0) <=u:
                left = mid+1
                # print(left,right,'ere',mid)
            else:
                right =mid-1
      
        if left < len(a):
            sec =a[left]-(a[l-2] if  l!=1 else 0)
            sect = a[left-1]-(a[l-2] if  l!=1 else 0)
        if  left < len(a)  and u*sec - ((sec-1)*sec)//2 > u*sect - ((sect-1)*sect)//2 :
            left +=1
        ans.append(left if left >l else l)
    print(*ans)
    
    
 
q = iinp()
# q = 1
for _ in range(q):
    solve()