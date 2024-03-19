class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pre=[]
        pre.append(0)
        hiphon=[]
        ans=[]
        for i in range(len(s)):
            if s[i]=='|':
                hiphon.append(i)
                pre.append(pre[-1])
            else:
                pre.append(pre[-1]+1)
        print(pre,hiphon)
        for que in queries:
            x = bisect_left(hiphon, que[0])
            y = bisect_right(hiphon, que[1])
            
            y-=1
            print(x,y)
            res=0
            if x<=y:
                res=pre[hiphon[y]]-pre[hiphon[x]]
            ans.append(res)

        return ans



            
        
        