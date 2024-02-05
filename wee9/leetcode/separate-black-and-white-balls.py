class Solution:
    def minimumSteps(self, s: str) -> int:
        m=0
        mu=1
        n=0
        while n<len(s) and s[n]!='1':
            n+=1
        n+=1
        while n<len(s):
            if s[n]=='0':
                m+=mu
            else:
                mu+=1
            n+=1
        return m


        