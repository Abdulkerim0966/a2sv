# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C



from re import M
import sys
 
 
def iinp():
    return int(sys.stdin.readline().strip())
 
 
def linp():
    return list(map(int, sys.stdin.readline().strip().split()))

solve():
    m, s = linp()
    if s==0 and m ==1:
        print(0,0)
        return
    
    if s> 9*m or s==0:
        print(-1,-1)
        return
    temp = s
    ma = []
    for i in range(m):
        if temp >= 9:
            ma.append('9')
            temp-=9
        else:
            ma.append(str(temp))
            temp-=temp
    ma=int(''.join(ma))
    mi=[]
    temp = s-1
    for i in range(m-1):
        if temp >= 9:
            mi.append('9')
            temp-=9
        else:
            mi.append(str(temp))
            temp-=temp
    temp += 1        
    mi.append(str(temp))
    mi.reverse()
    mi =int(''.join(mi))
    print(mi,ma)
    
        
        
    
    
 
# q = iinp()
q = 1
for _ in range(q):
    solve()