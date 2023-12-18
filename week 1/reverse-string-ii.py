class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s2=[]
        for i in range (len(s)):
            s2. append(s[i])  
        s1=[]
        space=1
        reverse=0
        for i in range (len(s2)):
            
            if i==len(s2)-1 and space<=k:
                left= reverse
                right=i
                while left<=right:
                    s2[right],s2[left]=s2[left],s2[right]
                    right-=1
                    left+=1
                for j in range (reverse,i+1,1):
                    s1.append(s2[j])
                


            elif space<k:
                space+=1
                
            elif k==space:
                left= reverse
                right=i
                while left<=right:
                    s2[right],s2[left]=s2[left],s2[right]
                    right-=1
                    left+=1
                for j in range (reverse,i+1, 1):
                    s1.append(s2[j])
                reverse+=2*k
                space+=1

            elif space>k and space<2*k:
                s1.append(s2[i])
                space+=1
            elif space==2*k:
                s1.append(s2[i])
                space=1

            

        return "".join(s1)
