# Problem: E - Yilal Doju - https://codeforces.com/gym/511242/problem/E

from math import ceil


n=int(input())
li=list(map(int,input().split()))
mi=float('inf')

for i in range(1,len(li)):
    att= ceil(li[i]/2)
    attp=ceil((li[i-1]-att)/2)
    
    
 
    cur = 0
    x = li[i]
    y = li[i - 1]
    if (x < y) :
        x, y=y,x
    
    cnt = min(x - y, (x + 1) / 2)
    cur += cnt
    x -= 2 * cnt
    y -= cnt
    if (x > 0 and y > 0) :
        cur += (x + y + 2) / 3
    
    mi= min(mi, cur);    
    
    # if attp<0:
    #     attp=0
    # mi=min(mi,(att+attp))
    # if li[i]%2==1 and (li[i-1]-att)%2==1:
    #     mi=min(mi,(att+attp)-1)

    if i<len(li)-1:
        att=min(li[i-1],li[i+1])
        att2=ceil(abs(li[i-1]-li[i+1])/2)
        mi=min(mi,(att+att2))
li.sort()

mi=min(mi,(ceil(li[0]/2)+ceil(li[1]/2)))
print(int(mi))