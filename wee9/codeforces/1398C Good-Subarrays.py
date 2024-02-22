from collections import Counter
for _ in range(int(input())):
    n=int(input())
    no=input()
    dect=Counter()
    pres=[]
    pres.append(0)
    ans=0
    for i in range(len(no)):
        pres.append(pres[i]+int(no[i]))
    
    for i in range(len(no)+1):
        if pres[i]-i in dect:
            ans+=dect[(pres[i]-i)]
        dect[pres[i]-i]+=1
    
    print(ans)
    5