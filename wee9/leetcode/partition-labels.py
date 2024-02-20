class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dect=Counter(s)

        temp=Counter()
        n=0
        ans=[]
        for i in range(len(s)):
            temp[s[i]]+=1
            if all(temp[key] == dect[key] for key in temp):
                # print(i,n)
                ans.append((i+1)-n)
                n=i+1
        return ans
