class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        stack2=[]
        for i in range (len(s)):
            if s[i]=="(":
                stack.append(s[i])
            elif len(stack)==0 and s[i]==")":
                stack2.append(s[i])
            else:
                stack.pop()
        return len(stack)+len(stack2)
        