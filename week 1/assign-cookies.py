class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        k=0
        pointer1=0
        pointer2=0
        while pointer1<len(g) and pointer2<len(s):
            if g[pointer1]>s[pointer2]:
                pointer2+=1
            else:
                k+=1
                pointer1+=1
                pointer2+=1
        return k
        