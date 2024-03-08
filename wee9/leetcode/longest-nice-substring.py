class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def checker(st):
            for i in st:
                if i.upper() not in st or i.lower() not in st:
                    return False
            return True
        ans=[]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if checker(s[i:j+1]):
                    if not ans or len(ans[0])<((j+1)-i):
                        if ans:
                            ans.pop()
                        ans.append(s[i:j+1])


        print (ans)
        return ''.join(ans)       
        

        