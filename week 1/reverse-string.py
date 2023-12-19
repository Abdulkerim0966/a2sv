class Solution:
    def reverseString(self, s: List[str]) -> None:
        lowe=0
        upp=len(s)-1
        for i in range (len(s)//2):
            s[lowe],s[upp]=s[upp],s[lowe]
            lowe+=1
            upp-=1