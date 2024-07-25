# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D



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
 
 



import sys, threading

input = lambda: sys.stdin.readline().strip()

    

def main():
    t= iinp()
    nums =linp()
    co =Counter(nums)
    
    memo ={}
    nums =sorted(set(nums))
    def dp(n):
        if n >=len(nums):
            return 0
    
        if n not in memo:
          
            if n+1<len(nums) and nums[n+1]-nums[n] !=1:
                memo[n] = dp(n+1) + co[nums[n]]*nums[n]
            else:
                right = dp(n+1)
                left = dp(n+2) + co[nums[n]]*nums[n]
                memo[n] = max(left,right)
        return memo[n]
    # dp(0)
    # print(memo)
    print(dp(0))
    

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

