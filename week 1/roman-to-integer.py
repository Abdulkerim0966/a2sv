class Solution:
    def romanToInt(self, s: str) -> int:
        count=0
        i=0
        while i<len(s):
            if s[i]=="I" :
                if i<len(s)-1 and s[i+1]=="V" :
                    count+=4
                    i+=2
                elif i<len(s)-1 and s[i+1]=="X":
                    count+=9
                    i+=2
                else :
                    count+=1
                    i+=1


            elif s[i]=="X":
                if i<len(s)-1 and s[i+1]=="L":
                    count+=40
                    i+=2
                elif i<len(s)-1 and s[i+1]=="C":
                    count+=90
                    i+=2
                else :
                    count+=10
                    i+=1


            elif s[i]=="C":
                if i<len(s)-1 and s[i+1]=="D":
                    count+=400
                    i+=2
                elif i<len(s)-1 and s[i+1]=="M":
                    count+=900
                    i+=2
                else :
                    count+=100
                    i+=1


            elif s[i]=="V":
                count+=5
                i+=1
            elif s[i]=="L":
                count+=50
                i+=1
            elif s[i]=="D":
                i+=1
                count+=500
            elif s[i]=="M":
                i+=1
                count+=1000
        return count

        