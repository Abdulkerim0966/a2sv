class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1="qwertyuiop"
        r2="asdfghjkl"
        r3="zxcvbnm"
        ans=[]
        for i in range(len(words)):
            r1f=False
            r2f=False
            r3f=False   
            for j in range(len(words[i])):
                if words[i][j].lower() in r1:
                    r1f=True
                   
                elif words[i][j].lower() in r2:
                    r2f=True
                    
                    
                elif words[i][j].lower() in r3:
                    r3f=True
                   
            if r1f==r2f==False or r1f==r3f==False or r2f==r3f==False:
                ans.append(words[i])
        return ans
        