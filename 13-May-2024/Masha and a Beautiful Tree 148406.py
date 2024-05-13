# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D



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
    nums= linp()
    count =0
    def merge(left,right):
        nonlocal count
        sorted_s = []
        if left[0] <= right[0]:  
            sorted_s.extend(left)
            sorted_s.extend(right)
            
        else:
            count+=1
            sorted_s.extend(right)
            sorted_s.extend(left)
            
        return sorted_s
        
    def mergesort(left,right,arr):
        if left == right:
            return [arr[left]]
        
        mid = left + (right - left) // 2
        
        left = mergesort(left, mid, arr)
        right = mergesort(mid + 1, right, arr)
        
        return merge(left, right)
        

    temp = mergesort(0,len(nums)-1,nums)
    print(count if temp == sorted(nums) else -1)

    
 
q = iinp()
# q = 1
for _ in range(q):
    solve()