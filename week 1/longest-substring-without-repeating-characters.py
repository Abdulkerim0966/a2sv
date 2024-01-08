class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        no=0
        l=[]
        t=1
        if len(s)==0:
            return 0
        for i in range(len(s)):
            l.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] not in l:
                    l.append(s[j])
                    t+=1
                    # print(l,no,t)
                    if no<t:
                        no=t
                else:
                    
                    if no<t:
                        no=t
                    t=1
                    l.clear()
                    break
        if no==0:
            return 1

        return no



        