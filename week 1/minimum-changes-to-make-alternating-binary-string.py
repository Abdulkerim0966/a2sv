class Solution:
    def minOperations(self, s: str) -> int:
        f1=False
        count1=0
        count0=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=='1':
                    count0+=1
                else:
                    count1+=1
            else:
                if s[i]=='0':
                    count0+=1
                else:
                    count1+=1
        return min(count1,count0)

        