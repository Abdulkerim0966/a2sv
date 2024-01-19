class Solution:
    def maxScore(self, s: str) -> int:
        one=s.count('1')
        ma=0
        for i in range(len(s)-1):
            if s[i]=='1':
                one-=1
                ma=max(ma,one)
            else:
                one+=1
                ma=max(ma,one)
        return ma