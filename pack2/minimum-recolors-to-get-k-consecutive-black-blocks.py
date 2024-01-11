class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mi=blocks[0:k].count('W')
        count=mi
        left=0
        for i in range(k,len(blocks)):
            if blocks[left]=='W':
              
                count-=1
                
            if blocks[i]=='W':
                count+=1
            left+=1
           
            mi=min(mi,count)
        return mi



        