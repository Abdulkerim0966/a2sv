class Solution:
    def minLength(self, s: str) -> int:
        count=0
        i=1
        while i <len(s):
            if (s[i]=='B' and s[i-1]=='A')or (s[i]=='D' and s[i-1]=='C'):
                s=(s[0:i-1]+s[i+1:])
                print(i,s)
                if i>1 :
                    i-=1
            else:
    
                i+=1

        return len(s)
        