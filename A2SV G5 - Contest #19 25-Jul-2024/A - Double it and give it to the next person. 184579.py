# Problem: A - Double it and give it to the next person. - https://codeforces.com/gym/527294/problem/A



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
    n =iinp()
    a = string()
    ans =[]
    i =0
    q=1
    while i < len(a):
        ans.append(a[i])
        
        
        i+=q
        q+=1
            
        
        
    return ''.join(ans)
                
    
    
 
# q = iinp()
q = 1
for _ in range(q):
    print(solve())