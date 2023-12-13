class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans=defaultdict(int)
        sites=[]
        for i in range(len(cpdomains)):

            no,site=cpdomains[i].split()
            dect=Counter(site)
            if dect['.']==2:
                a,b,c=site.split('.')
                ans[a+'.'+b+'.'+c]+=int(no)
                ans[b+'.'+c]+=int(no)
                ans[c]+=int(no)
            else:
                a,b,=site.split('.')
                ans[a+'.'+b]+=int(no)
                ans[b]+=int(no)
        for i in ans:
            sites.append(str(ans[i])+' '+i)




               
                
        return sites

            

        