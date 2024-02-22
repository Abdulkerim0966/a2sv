class Solution:
    def removeStars(self, s: str) -> str:
        re=[]
        # last=-1
        for i in range (len(s)):
            if s[i]=="*":
                re.pop()
                # last-=1
            else :
                re.append(s[i])
                # last+=1
        return ''.join(re)
        