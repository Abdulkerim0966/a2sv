class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans=[]
        dect={}
        for i in range (len(paths)):
            path=list(paths[i].split())
            
            for j in range(1,len(path)):
                begin=path[j].index('(') +1
                if path[j][begin:-1] in dect:
                    dect[path[j][begin:-1]]+=[path[0]+"/"+(path[j][0:begin-1])]

                else:
                    dect[path[j][begin:-1]]=[path[0]+'/'+(path[j][0:begin-1])]
        
        for pat in dect:
            if len(dect[pat])>1:
                ans.append(dect[pat])
        return ans