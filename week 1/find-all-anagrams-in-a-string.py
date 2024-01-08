class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dect=defaultdict(int)
        for i  in range(len(p)):
            dect[p[i]]+=1
        p2=len(p)
        ans=[]
        # print(dect)

        for i in range(len(s)-(p2-1)):
            f1=False
            for ch in dect:
                # print(s[i:i+p2])
                if s[i:i+p2].count(ch)!=dect[ch]:
                    f1=True
                    break
            if f1==False:
                ans.append(i)  
        return ans

       
